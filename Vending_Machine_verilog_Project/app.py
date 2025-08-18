from flask import Flask, render_template, request, send_from_directory
import subprocess
import os
import datetime
import shutil

# Import your database functions here
from database import init_db, insert_transaction

app = Flask(__name__)

# Initialize DB once at startup
init_db()

# Home page
@app.route('/')
def index():
    synthesis_image = None
    if os.path.exists("static/vending_machine.png"):
        synthesis_image = "vending_machine.png"
    return render_template('index.html', synthesis_image=synthesis_image)


# Handle user simulation from form
@app.route('/simulate', methods=['POST'])
def simulate():
    product = request.form['product']
    money = request.form['money']

    # Validate inputs (basic)
    try:
        product_code = int(product)
        money_in = int(money)
    except ValueError:
        return render_template("index.html", error="Invalid input! Enter numeric values.")

    # Set environment variables for simulation
    env = os.environ.copy()
    env["PRODUCT_CODE"] = str(product_code)
    env["MONEY_IN"] = str(money_in)

    # Append simulation logs to a fixed file
    sim_log_file = "simulation_log.txt"
    with open(sim_log_file, "a") as f:
        f.write("\n\n===== Simulation Run at: {} =====\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        subprocess.run([
            "make",
            "MODULE=test_vending_machine",
            "TESTCASE=test_user_transaction"
        ], env=env, stdout=f, stderr=subprocess.STDOUT)

    # Parse simulation output results (from ui_result.txt)
    result = {}
    result_file = "ui_result.txt"
    if os.path.exists(result_file):
        with open(result_file, "r") as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=")
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                    result[key] = val

    synthesis_image = None
    if os.path.exists("static/vending_machine.png"):
        synthesis_image = "vending_machine.png"

    # Map product code to name
    product_names = {
        0: 'Coke',
        1: 'Oreo',
        2: 'Lays Chips',
        3: 'Dairy Milk',
        4: 'Melody',
        5: 'KitKat'
    }
    product_name = product_names.get(product_code, "Unknown")

    # Insert transaction into DB
    insert_transaction(
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        product_code=product_code,
        product_name=product_name,
        money_in=money_in,
        dispense=result.get('Dispense', 0),
        change=result.get('Change', 0),
        out_of_stock=result.get('OutOfStock', 0),
        log_file=sim_log_file,
        synthesis_image=synthesis_image
    )

    return render_template("index.html", result=result, synthesis_image=synthesis_image)


# Handle batch test run and append the output to a fixed log file
@app.route('/run_batch_tests', methods=['POST'])
def run_batch_tests():
    log_file = "batch_tests_log.txt"  # Fixed log file name

    with open(log_file, "a") as f:  # Append mode
        # Write timestamp header
        f.write("\n\n===== Batch Test Run at: {} =====\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        subprocess.run([
            "make", "MODULE=test_vending_machine_all"
        ], stdout=f, stderr=subprocess.STDOUT)

    synthesis_image = None
    if os.path.exists("static/vending_machine.png"):
        synthesis_image = "vending_machine.png"

    # Insert batch test run in DB
    insert_transaction(
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        product_code=None,
        product_name="Batch Test Run",
        money_in=None,
        dispense=None,
        change=None,
        out_of_stock=None,
        log_file=log_file,
        synthesis_image=synthesis_image
    )

    return render_template("index.html", batch_result=log_file, synthesis_image=synthesis_image)


# Run synthesis and save PNG to static folder
@app.route('/run_synthesis', methods=['POST'])
def run_synthesis():
    # Run Yosys synthesis command
    subprocess.run([
        "yosys", "-p",
        "read_verilog vending_machine.v; synth -top vending_machine; show -format png -prefix vending_machine"
    ])

    # Move PNG to static folder for serving
    png_file = "vending_machine.png"
    if os.path.exists(png_file):
        shutil.move(png_file, os.path.join("static", png_file))
        synthesis_image = png_file
    else:
        synthesis_image = None

    # Insert synthesis event in DB
    insert_transaction(
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        product_code=None,
        product_name="Synthesis Run",
        money_in=None,
        dispense=None,
        change=None,
        out_of_stock=None,
        log_file=None,
        synthesis_image=synthesis_image
    )

    return render_template("index.html", synthesis_image=synthesis_image)


# View log file content
@app.route('/view_log/<filename>')
def view_log(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f"<pre>{f.read()}</pre>"
    else:
        return "Log file not found!"


# Launch GTKWave waveform viewer
@app.route('/view_waveform')
def view_waveform():
    vcd_file = "dump.vcd"

    if os.path.exists(vcd_file):
        try:
            subprocess.Popen(["gtkwave", vcd_file])
            return "GTKWave has been launched on your system!"
        except Exception as e:
            return f"Failed to open GTKWave: {str(e)}"
    else:
        return "Waveform file not found!"


if __name__ == '__main__':
    app.run(debug=True)
