from myhdl import *
from TypeDecode import TypeDecode
from ControlDecode import controlDecode

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
    cd = controlDecode(*types, MemWrite,Branch,MemRead,RegWrite,MemToReg,Operand_b_Sel,AluOp,Operand_a_Sel,ExtendSel,NextPcSel)

    return itd,cd



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