# test_vending_machine_all.py
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def vending_machine_test(dut):
    """Runs all test cases for the vending machine logic including stock and out_of_stock."""

    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset the DUT and initialize inputs
    dut.reset.value = 1
    dut.money_in.value = 0
    dut.product_code.value = 0
    await Timer(10, units="ns")
    dut.reset.value = 0

    dut._log.info("========== VENDING MACHINE TEST STARTED ==========")

    async def run_test(money, product_code, desc):
        dut._log.info(desc)
        dut.money_in.value = money
        dut.product_code.value = product_code
        await RisingEdge(dut.clk)
        await Timer(5, units="ns")

        dispense = int(dut.dispense.value)
        change = int(dut.change.value)
        out_of_stock = int(dut.out_of_stock.value)

        dut._log.info(f"Dispensed: {dispense}, Change Returned: ₹{change}, Out of Stock: {out_of_stock}")

        return dispense, change, out_of_stock

    # -------- TEST CASES --------
    await run_test(15, 0b000, "Test Case 1: Buy Product A (₹15) with ₹15")

    # Explicit out of stock test case for product 1 which has stock=0
    dispense, change, out_of_stock = await run_test(10, 0b001,
                                                    "Test Case 2: Buy Product B (₹5) with ₹10 — Expect Out of Stock since stock=0")
    assert dispense == 0, "Expected dispense=0 for out of stock product"
    assert out_of_stock == 1, "Expected out_of_stock=1 for out of stock product"

    await run_test(8, 0b010, "Test Case 3: Buy Product C (₹10) with ₹8 — Insufficient Money")
    await run_test(5, 0b011, "Test Case 4: Buy Product D (₹5) with ₹5 — Exact Money")
    await run_test(15, 0b111, "Test Case 5: Invalid Product Code (111) with ₹20")

    # -------- STOCK DEPLETION TEST --------
    dut._log.info("Testing stock depletion for Product D (code 3)")

    # 1st purchase - should dispense successfully, stock goes from 1 to 0
    await run_test(5, 0b011, "Depleting stock: 1st purchase of Product D with ₹5")

    # 2nd purchase - stock should now be 0, expect out_of_stock=1
    dispense, change, out_of_stock = await run_test(5, 0b011,
                                                    "Depleting stock: 2nd purchase attempt of Product D with ₹5 — Expect Out of Stock")
    assert dispense == 0, "Expected dispense=0 after stock depleted"
    assert out_of_stock == 1, "Expected out_of_stock=1 after stock depleted"

    dut._log.info("========== VENDING MACHINE TEST ENDED ==========")
