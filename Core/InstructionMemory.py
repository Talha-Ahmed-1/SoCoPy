from myhdl import *

DW = 32
AW = DW/4

@block
def InstructionMemory(addr, inst_out, INSTRUCTIONS):
    
    @always_comb
    def read():
        inst_out.next = INSTRUCTIONS[int(addr)]
    return read