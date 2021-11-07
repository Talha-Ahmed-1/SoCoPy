from myhdl import *

@block
def ImmediateGeneration(
                        inst,
                        pc,
                        s_imm,
                        sb_imm,
                        uj_imm,
                        u_imm,
                        i_imm
                        ):
    
    @always_comb
    def generate():
        i_imm.next = concat(intbv(inst[31])[20:],inst[32:20])
        s_imm.next = concat(intbv(inst[31])[20:], inst[32:25], inst[12:7])
        u_imm.next = concat(inst[32:12], intbv(0)[11:])
        sb_imm.next = concat(intbv(inst[31])[19:], inst[31], inst[7], inst[31:25], inst[12:8], intbv(0)[1:]) + pc
        uj_imm.next = concat(intbv(inst[31])[12:], inst[20:12], inst[20], inst[31:21], intbv(0)[1:]) + pc
    
    return generate

DW = 2**31


@block
def Simulate():



    inst = Signal(intbv(0, 0, DW)[32:])
    pc = Signal(intbv(0, 0, DW))
    s_imm = Signal(intbv(0, -DW, DW))
    sb_imm = Signal(intbv(0, -DW, DW))
    uj_imm = Signal(intbv(0, -DW, DW))
    u_imm = Signal(intbv(0, -DW, DW))
    i_imm = Signal(intbv(0, -DW, DW))

    immGen = ImmediateGeneration(inst, pc, s_imm, sb_imm, uj_imm, u_imm, i_imm)

    # test case of instruction lists
    instList = [0xffc00393, 0x00400393]

    @instance
    def run():
        for _ in instList:
            inst.next = _
            pc.next = 0x00000000
            yield delay(10)
            print("inst: ", inst)
            print("s_imm: ", s_imm)
            print("sb_imm: ", (sb_imm))
            print("uj_imm: ", (uj_imm))
            print("u_imm: ", u_imm)
            print("i_imm: ", (i_imm))
            print("pc: ", pc)
            print("")

    return run, immGen

# tb = Simulate()
# tb.run_sim()


# Only run when u want verilog of this module
def toGenerateVerilog():
    inst = Signal(intbv(0, 0, DW))
    pc = Signal(intbv(0, 0, DW))
    s_imm = Signal(intbv(0, -DW, DW))
    sb_imm = Signal(intbv(0, -DW, DW))
    uj_imm = Signal(intbv(0, -DW, DW))
    u_imm = Signal(intbv(0, -DW, DW))
    i_imm = Signal(intbv(0, -DW, DW))

    immGen = ImmediateGeneration(inst, pc, s_imm, sb_imm, uj_imm, u_imm, i_imm)
    immGen.convert('Verilog')

# uncomment to generate verilog
# toGenerateVerilog()
