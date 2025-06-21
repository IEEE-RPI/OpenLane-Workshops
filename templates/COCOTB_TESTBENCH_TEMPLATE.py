# cocotb testbench template for HDL IP
import cocotb
from cocotb.triggers import RisingEdge

async def source(dut):
    """Drive stimulus to the DUT."""
    # TODO: add driving logic
    await RisingEdge(dut.clk)

async def drain(dut):
    """Consume outputs from the DUT."""
    # TODO: add checking logic
    await RisingEdge(dut.clk)

@cocotb.test()
async def run_test(dut):
    """Example test that uses source and drain."""
    await source(dut)
    await drain(dut)

