import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import os

@cocotb.test()
async def test_user_transaction(dut):
    """Simulates a user transaction by reading env variables for 6 products."""

    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset DUT
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    # Read environment variables
    product_code = int(os.getenv("PRODUCT_CODE", "0"))
    money_in = int(os.getenv("MONEY_IN", "0"))

    # Clamp product_code to 0..5 (valid products)
    if product_code < 0 or product_code > 5:
        product_code = 0  # fallback to default product 0

    dut.product_code.value = product_code
    dut.money_in.value = money_in

    # Wait for clock edge and settle time
    await RisingEdge(dut.clk)
    await Timer(5, units="ns")

    # Read outputs
    dispense = int(dut.dispense.value)
    change = int(dut.change.value)
    out_of_stock = int(dut.out_of_stock.value)

    # Log info
    dut._log.info(f"INPUT: product_code={product_code}, money_in={money_in}")
    dut._log.info(f"OUTPUT: dispense={dispense}, change={change}, out_of_stock={out_of_stock}")

    # Save to file for dashboard/UI
    with open("ui_result.txt", "w") as f:
        f.write(f"ProductCode={product_code}\n")
        f.write(f"MoneyIn={money_in}\n")
        f.write(f"Dispense={dispense}\n")
        f.write(f"Change={change}\n")
        f.write(f"OutOfStock={out_of_stock}\n")
