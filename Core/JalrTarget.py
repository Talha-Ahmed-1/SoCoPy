from myhdl import *

@block
def JalrTarget(a,b,out):

    @always_comb
    def comb():
        out.next = intbv(((a + b) & 7177314461492))[32:] 
    return comb

a = Signal(intbv(0)[32:])
b = Signal(intbv(0)[32:])
out = Signal(intbv(0)[32:])
jalr = JalrTarget(a,b,out)
jalr.convert(hdl='Verilog')


# import random
# @block
# def testbench():

#     a,b,o = [Signal(intbv(0,min=0, max=(2**32)-1)) for i in range(3)]
#     j = JalrTarget(a,b,o)

#     @instance
#     def stimulus():
#         print("a b o")
#         for i in range(10):
#             a.next = random.randrange(2**32)
#             b.next = random.randrange(2**32)
#             yield delay(10)
#             print(int(a),int(b),int(o))
#         raise StopSimulation
    
#     return j, stimulus

# tb = testbench()
# tb.run_sim()