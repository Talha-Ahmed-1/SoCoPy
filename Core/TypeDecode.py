from myhdl import *
import random

@block
def TypeDecode(opCode, RType, Load, Store, Branch, IType, Jalr, Jal, Lui):

    @always_comb
    def comb():
        # RType.next,Load.next, Store.next, Branch.next, IType.next, Jalr.next, Jal.next, Lui.next = [False for i in range(8)]
        
        
        if opCode == 51:
            RType.next = 1
        elif opCode == 3:
            Load.next = 1
        elif opCode == 35:
            Store.next = 1
        elif opCode == 99:
            Branch.next = 1
        elif opCode == 19:
            IType.next = 1
        elif opCode == 103:
            Jalr.next = 1
        elif opCode == 111:
            Jal.next = 1
        elif opCode == 55:
            Lui.next = 1
        
    return comb

opCodes = [51,3,35,99,19,103,111,55]
types = [Signal(bool(0)) for i in range(8)]
opCode = Signal(intbv(0, min=0, max=112))

itd_1 = TypeDecode(opCode, *types)
itd_1.convert('Verilog')
# @block
# def itdTest():

#     types = [Signal(bool(0)) for i in range(8)]
#     opCode = Signal(intbv(0, min=0, max=112))

#     itd_1 = typeDecode(opCode, *types)

#     @instance
#     def stimulus():
#         fmt = "{0:6} | {1:5} | {2:5} | {3:5} | {4:6} | {5:5} | {6:5} | {7:5} | {8:5}"
#         print(fmt.format("OpCode","RType", "Load", "Store", "Branch", "IType", "Jalr","Jal", "Lui"))
#         for i in range(10):
#             opCode.next = random.choice(opCodes)
#             yield delay(10)
#             print(fmt.format(str(int(opCode)), *[str(type) for type in types]))
#         raise StopSimulation
    
#     return itd_1, stimulus

# tb = itdTest()
# tb.run_sim()