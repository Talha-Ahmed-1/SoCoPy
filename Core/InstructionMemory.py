from myhdl import *

DW = 32
AW = DW/4

def loadmemoryfromfile(pathToFile):
    file = open(pathToFile, "r")
    return tuple([int("0x"+inst, 16) for inst in open(pathToFile, "r").read().split("\n")])

@block
def InstructionMemory(addr, inst_out, INSTRUCTIONS):
    
    ## FIXME: Introduce read from file inst. """FIXED"""
    # mem = [Signal(intbv(INSTRUCTIONS[i], 0, 2**DW)) for i in range(len(INSTRUCTIONS))]
    # mem = [Signal(intbv(i, 0, 2**DW)) for i in loadmemoryfromfile(INSTRUCTIONS)]
    @always_comb
    def read():
        inst_out.next = INSTRUCTIONS[int(addr)]
    return read