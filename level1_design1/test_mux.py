# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    A = 0
    B = 1
    C = 2
    D = 3
     
    SEL= 30

    dut.inp30.value = D
    dut.sel.value = SEL
    await Timer(2, units='ns')


    cocotb.log.info(f'INP30={D} SEL={SEL} model={D} DUT={int(dut.out.value)}')
    assert dut.out.value == D, f'MUX result is incorrect: {dut.out.value} !=D'