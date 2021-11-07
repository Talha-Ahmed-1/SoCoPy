from myhdl import *

ROWS = 32
DW = 2**(ROWS-1)

@block
def RegisterFile(
                clock,
                regWrite,
                wd,
                ws,
                rs1,
                rs2,
                rd1,
                rd2
                ):

    register = [Signal(intbv(0, -DW, DW)) for i in range(ROWS)]
    # register[0] = Signal(intbv(0, -DW, DW))
    
    @always_comb
    def read():
        rd1.next = register[int(rs1)]
        rd2.next = register[int(rs2)]

    @always(clock.posedge)
    def write():
        if regWrite & int(ws) != 0:
            register[int(ws)].next = wd


    return read, write