from myhdl import *

ADD = intbv(0)
SLL, SLLI = [intbv(1)] * 2
SLT, SLTI = [intbv(2)] * 2
SLTU, SLTUI, BLTU = [intbv(3)] * 3
XOR, XORI = [intbv(4)] * 2
SRL, SRLI = [intbv(5)] * 2
OR, ORI = [intbv(6)] * 2
AND, ANDI = [intbv(7)] * 2
SUB = intbv(8)
SRA, SRAI = [intbv(13)] * 2
BEQ = intbv(16)
BNE = intbv(17)
BLT = intbv(20)
BGE = intbv(21)
BLTU = intbv(22)
BGEU = intbv(23)
JAL, JALR = [intbv(31)] * 2

DW = 2**32
@block
def ALU(in1, in2, control, out):

    @always_comb
    def run():
        if control == 0:
            out.next = in1 + in2
        elif control == 1:
            out.next = in1 << in2
        elif control == 2 and control == 3 and control == 22:
            out.next = in1 < in2
        elif control == 4:
            out.next = in1 ^ in2
        elif control == 5 and control == 13:
            out.next = in1 >> in2[5:0]
        elif control == 6:
            out.next = in1 | in2
        elif control == 7:
            out.next = in1 & in2
        elif control == 8:
            out.next = in1 - in2
        # elif control == 13:
        #     out.next = in1 >> in2[5:0]
        elif control == 16:
            out.next = in1 == in2
        elif control == 17:
            out.next = in1 != in2
        elif control == 20:
            out.next = in1 < in2
        elif control == 21 and control == 23:
            out.next = in1 >= in2
        elif control == 31:
            out.next = in1

    return run

in1 = Signal(intbv(0, -DW, DW))
in2 = Signal(intbv(0, -DW, DW))
out = Signal(intbv(0, -DW, DW))
control = Signal(intbv(0, 0, 32))

alu = ALU(in1, in2, control, out)
# alu.convert('Verilog')