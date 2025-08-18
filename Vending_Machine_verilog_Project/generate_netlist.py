import subprocess
import os
import webbrowser

# File paths
verilog_file = "vending_machine.v"
json_netlist_file = "vending_machine_netlist.json"
svg_output_file = "vending_machine_netlist.svg"

# Yosys synthesis command (gate-level netlist for netlistsvg)
yosys_cmd = f"""
read_verilog {verilog_file}
hierarchy -top vending_machine
proc
flatten
opt
techmap
write_json {json_netlist_file}
"""

def run_synthesis():
    try:
        print("🔄 Running synthesis...")
        result = subprocess.run(
            ["yosys", "-p", yosys_cmd],
            capture_output=True,
            text=True
        )

        if result.returncode != 0 or "ERROR" in result.stdout or "ERROR" in result.stderr:
            print("❌ Synthesis failed!")
            print(result.stdout)
            print(result.stderr)
            return False

        if not os.path.exists(json_netlist_file) or os.path.getsize(json_netlist_file) == 0:
            print("❌ Netlist file missing or empty!")
            return False

        print("✅ Synthesis completed successfully!")
        return True

    except FileNotFoundError:
        print("❌ Yosys not found! Install Yosys and ensure it’s in your PATH.")
        return False

def generate_svg():
    try:
        print("📐 Generating SVG diagram from netlist...")
        subprocess.run(
            ["netlistsvg", json_netlist_file, "-o", svg_output_file],
            check=True
        )
        if os.path.exists(svg_output_file) and os.path.getsize(svg_output_file) > 0:
            print(f"✅ SVG generated: {os.path.abspath(svg_output_file)}")
            # Automatically open SVG in default browser
            webbrowser.open(f"file://{os.path.abspath(svg_output_file)}")
        else:
            print("❌ SVG generation failed!")

    except FileNotFoundError:
        print("❌ netlistsvg not found! Install it using: npm install -g netlistsvg")

if __name__ == "__main__":
    if run_synthesis():
        generate_svg()
