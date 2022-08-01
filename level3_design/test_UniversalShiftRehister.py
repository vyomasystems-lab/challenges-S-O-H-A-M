# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test() 
async def test_UniversalShiftRegister(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    #reset
    dut.b.value=0b0011
    dut.clk.value=0
    dut.s1.value=1
    dut.s0.value=1
    dut.r_in.value=1
    dut.l_in.value=1
    await FallingEdge(dut.clk)  
    dut.s1.value=0
    dut.s0.value=0
    await FallingEdge(dut.clk)  
    dut.s1.value=1
    dut.s0.value=0
    r_in=1;l_in=1 
    """ Leftshift-10->if l_in=1 1ast bit after left shift will be 1 else if lin=0 1ast bit after left shift will be 0 """
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    await FallingEdge(dut.clk)  
    r_in=0
    l_in=1
    dut.s1.value=0
    dut.s0.value=0
    await FallingEdge(dut.clk)  
    r_in=1
    l_in=1
    dut.s1.value=0
    dut.s0.value=1
    await FallingEdge(dut.clk)  
