from myhdl import *

ROWS = 1024
DW = 2**31

@block
def DataMemory(clk, addr, data_in, data_out, we, rd):

    mem = [Signal(intbv(0, -DW, DW)) for i in range(ROWS)]

    @always(clk.posedge)
    def read():
        # if rd:
        data_out.next = mem[int(addr)]  & (rd << 32)

    @always(clk.posedge)
    def write():
        # if we:
        mem[addr].next = data_in & (we << 32)

    return read, write

def toGenerateVerilog():
    clk = Signal(bool(0))
    addr = Signal(intbv(0)[10:])
    data_in = Signal(intbv(0, -DW, DW)[32:])
    data_out = Signal(intbv(0, -DW, DW)[32:])
    we = Signal(bool(0))
    rd = Signal(bool(0))
    # mem_data = Signal(intbv(0)[32:])

    dmem = DataMemory(clk, addr, data_in, data_out, we, rd)

    dmem.convert('Verilog')

toGenerateVerilog()