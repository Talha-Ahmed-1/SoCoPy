from myhdl import *

DW = 32

@block
def PC(clock, input, pc, pc4):

    reg = Signal(modbv(0,0,2**DW))
    @always_comb
    def read():
        pc.next = reg
        pc4.next = reg + 4
    
    @always(clock.posedge)
    def write():
        reg.next = input

    return read, write