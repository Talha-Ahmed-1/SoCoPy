from myhdl import *

@block
def controlDecode(
                    RType,
                    Load,
                    Store,
                    SBType,
                    IType,
                    Jalr,
                    Jal,
                    Lui,
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

    @always_comb
    def comb():
        MemWrite.next, Branch.next, MemRead.next, RegWrite.next, MemToReg.next, Operand_b_Sel.next = [False for i in range(6)]
        AluOp.next, Operand_a_Sel.next, ExtendSel.next, NextPcSel.next = [0 for i in range(4)]

        if RType == True:
            RegWrite.next = True
        elif Load == True:
            MemRead.next, RegWrite.next, MemToReg.next, Operand_b_Sel.next = [True for i in range(4)]
            AluOp.next = 4
        elif Store == True:
            MemWrite.next, Operand_b_Sel.next = [True for i in range(2)]
            AluOp.next = 5
            ExtendSel.next = 2
        elif SBType == True:
            Branch.next = True
            AluOp.next = 2
            NextPcSel.next = 1
        elif IType == True:
            RegWrite.next, Operand_b_Sel.next = [True for i in range(2)]
            AluOp.next = 1
        elif Jalr == True:
            RegWrite.next = True
            AluOp.next = 3
            Operand_a_Sel.next = 2
            NextPcSel.next = 3
        elif Jal == True:
            RegWrite.next, Operand_b_Sel.next = [True for i in range(2)]
            AluOp.next = 3
            Operand_a_Sel.next = 2
            NextPcSel.next = 2
        elif Lui == True:
            RegWrite.next, Operand_b_Sel.next = [True for i in range(2)]
            AluOp.next = 6
            Operand_a_Sel.next = 3
            ExtendSel.next = 1


    return comb


# opCodes = [51,3,35,99,19,103,111,55]
# from typeDecode import typeDecode
# import random
# @block
# def itdTest():

#     types = [Signal(bool(0)) for i in range(8)]
#     opCode = Signal(intbv(0, min=0, max=112))
#     bool_signals = [Signal(bool(0)) for i in range(6)]
#     int_signals = [Signal(intbv(0)) for i in range(4)]

#     itd_1 = typeDecode(opCode, *types)
#     cd = controlDecode(*types, *bool_signals, *int_signals )

#     @instance
#     def stimulus():
#         # fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5} | {9:100} |"
#         print("OpCode","RType", "Load", "Store", "Branch", "IType", "Jalr","Jal", "Lui", "oo")
#         for i in opCodes:
#             opCode.next = i #random.choice(opCodes)
#             yield delay(10)
#             print(str(int(opCode)) ,[[str(b) for b in bool_signals],[str(i) for i in int_signals]] )
#         raise StopSimulation
    
#     return itd_1, cd, stimulus

# tb = itdTest()
# tb.run_sim()