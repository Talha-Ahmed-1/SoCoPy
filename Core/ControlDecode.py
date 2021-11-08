from myhdl import *

@block
def ControlDecode(
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

    # @always(Signal(bool(0)))
    @always_comb
    def comb():
        # RType.next = 0
        # Load.next = 0
        # Store.next = 0
        # SBType.next = 0
        # IType.next = 0
        # Jalr.next = 0
        # Jal.next = 0
        # Lui.next = 0
        # MemWrite.next = 0
        # Branch.next = 0
        # MemRead.next = 0
        # RegWrite.next = 0
        # MemToReg.next = 0
        # Operand_b_Sel.next = intbv(0)
        # AluOp.next = intbv(0)
        # Operand_a_Sel.next = intbv(0)
        # ExtendSel.next = intbv(0)
        # NextPcSel.next = intbv(0)


        # MemWrite.next, Branch.next, MemRead.next, RegWrite.next, MemToReg.next, Operand_b_Sel.next = [False for i in range(6)]
        # AluOp.next, Operand_a_Sel.next, ExtendSel.next, NextPcSel.next = [0 for i in range(4)]

        if RType == 1:
            RegWrite.next = 1
        elif Load == 1:
            # MemRead.next, RegWrite.next, MemToReg.next, Operand_b_Sel.next = [1]*4#[1 for i in range(4)]
            MemRead.next = 1
            RegWrite.next = 1
            MemToReg.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(4,0)   
        elif Store == 1:
            # MemWrite.next, Operand_b_Sel.next = [1]*2 #[1 for i in range(2)]
            MemWrite.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(5,0) 
            ExtendSel.next = intbv(2,0) 
        elif SBType == 1:
            Branch.next = 1
            AluOp.next = intbv(2,0) 
            NextPcSel.next = intbv(1,0) 
        elif IType == 1:
            # RegWrite.next, Operand_b_Sel.next = [1]*2 #[1 for i in range(2)]
            RegWrite.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(1,0) 
        elif Jalr == 1:
            RegWrite.next = 1
            AluOp.next = intbv(3,0) 
            Operand_a_Sel.next = intbv(2,0)
            NextPcSel.next = intbv(3,0)
        elif Jal == 1:
            # RegWrite.next, Operand_b_Sel.next = [1]*2 #[1 for i in range(2)]
            RegWrite.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(3,0)
            Operand_a_Sel.next = intbv(2,0)
            NextPcSel.next = intbv(2,0)
        elif Lui == 1:
            # RegWrite.next, Operand_b_Sel.next = [1]*2 #[1 for i in range(2)]
            RegWrite.next = 1
            Operand_b_Sel.next = 1
            AluOp.next = intbv(6,0)
            Operand_a_Sel.next = intbv(3,0)
            ExtendSel.next = intbv(1,0)


    return comb

RType = Signal(bool(0))
Load = Signal(bool(0))
Store = Signal(bool(0))
SBType = Signal(bool(0))
IType = Signal(bool(0))
Jalr = Signal(bool(0))
Jal = Signal(bool(0))
Lui = Signal(bool(0))
MemWrite = Signal(bool(0))
Branch = Signal(bool(0))
MemRead = Signal(bool(0))
RegWrite = Signal(bool(0))
MemToReg = Signal(bool(0))
Operand_b_Sel = Signal(intbv(0,min=0)[2:])
AluOp = Signal(intbv(0,min=0)[3:])
Operand_a_Sel = Signal(intbv(0,min=0)[2:])
ExtendSel = Signal(intbv(0,min=0)[2:])
NextPcSel = Signal(intbv(0,min=0)[2:])

ControlDecode_inst = ControlDecode(
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
                                )
ControlDecode_inst.convert(hdl='Verilog')

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
#     cd = ControlDecode(*types, *bool_signals, *int_signals )

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