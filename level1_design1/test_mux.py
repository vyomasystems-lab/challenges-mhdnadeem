# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    INP5 = 2
    SEL= 4

    dut.inp5.value = INP5
    dut.sel.value = SEL
    await Timer(2, units='ns')


    cocotb.log.info(f'INP5={INP5} SEL={SEL} model={2} DUT={int(dut.out.value)}')
    assert dut.out.value == 2, f'MUX result is incorrect: {dut.out.value} !=2'