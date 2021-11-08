from myhdl import *
from TypeDecode import TypeDecode
from ControlDecode import ControlDecode

@block 
def ControlUnit(opCode,
                MemWrite,
                Branch,
                MemRead,
                RegWrite,
                MemToReg,
                Operand_b_Sel,
                AluOp,
                Operand_a_Sel,
                ExtendSel,
                NextPcSel
                ):

    types = [Signal(bool(0)) for i in range(8)]

    itd = TypeDecode(opCode, *types)
    cd = ControlDecode(*types, MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Operand_a_Sel,ExtendSel,NextPcSel)

    return itd,cd

opCode = Signal(intbv(0)[32:])
MemWrite = Signal(bool(0))
Branch = Signal(bool(0))
MemRead = Signal(bool(0))
RegWrite = Signal(bool(0))
MemToReg = Signal(bool(0))
Operand_b_Sel = Signal(bool(0))
AluOp = Signal(bool(0))
Operand_a_Sel = Signal(bool(0))
ExtendSel = Signal(bool(0))
NextPcSel = Signal(bool(0))

control = ControlUnit(opCode, MemWrite, Branch, MemRead, RegWrite, MemToReg, Operand_b_Sel, AluOp, Operand_a_Sel, ExtendSel, NextPcSel)
control.convert('Verilog')

# TESTBENCH
# opCodes = [51,3,35,99,19,103,111,55]
# import random
# @block
# def testbench():
#     opCode = Signal(intbv(0, min=0, max=112))
#     bool_signals = [Signal(bool(0)) for i in range(6)]
#     int_signals = [Signal(intbv(0)) for i in range(4)]
#     cu = ControlUnit(opCode, *bool_signals, *int_signals)

#     @instance
#     def stimulus():
#         for i in opCodes:
#             opCode.next = i
#             yield delay(10)
#             print(str(int(opCode)) ,[[str(b) for b in bool_signals],[str(i) for i in int_signals]] )

#         raise StopSimulation

#     return cu,stimulus

# tb = testbench()
# tb.run_sim()