from myhdl import *
from PC import PC
# from Common.loadmemoryfromfile import loadmemoryfromfile
from InstructionMemory import InstructionMemory
from Control import ControlUnit
from RegisterFile import RegisterFile
from ImmediateGeneration import ImmediateGeneration
from AluCtrl import AluControl
from Alu import ALU
from JalrTarget import JalrTarget
from DataMemory import DataMemory

def loadmemoryfromfile(pathToFile):
    file = open(pathToFile, "r")
    return tuple([int("0x"+inst, 16) for inst in open(pathToFile, "r").read().split("\n")])

@block
def Core(clk,reset_n):

    @always_seq(clk.posedge, reset=reset_n)
    def top():

        pc_in, pc_out, pc4_out = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(3)]
        pc = PC(clk, pc_in, pc_out, pc4_out)

        instructions = loadmemoryfromfile("/home/talha/SoCoPy/Instruction.txt")
        inst_out = Signal(intbv(0, min=0 ,max=(2**32)-1))
        instr_memory = InstructionMemory(pc_out, inst_out, instructions)

        #                   [  MemWrite, Branch, MemRead, RegWrite, MemToReg, Operand_b_Sel ]
        ctrl_bool_signals = [Signal(bool(0)) for i in range(6)]
        #                   [ AluOp, Operand_a_Sel, ExtendSel, NextPcSel ]
        ctrl_int_signals = [Signal(intbv(0)) for i in range(4)]
        control = ControlUnit(inst_out[6:], *ctrl_bool_signals, *ctrl_int_signals)

        reg_write_data, reg_read_data1, reg_read_data2 = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(3)]
        reg_file = RegisterFile(clk, ctrl_bool_signals[3],reg_write_data, inst_out[11,7], inst_out[19:15], inst_out[24:20], reg_read_data1, reg_read_data2)

        #       [ S_Imm, SB_Imm, UJ_Imm, U_Imm, I_Imm ]
        imms = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(5)]
        imm_gen = ImmediateGeneration(inst_out, pc_out, *imms )

        alu_ctrl_pin = Signal(intbv(0, min=0, max=(2**5)-1))
        AluControl(ctrl_int_signals[0], inst_out[14:12], inst_out[30], alu_ctrl_pin)

        alu_a, alu_b = [Signal(intbv(0, min=0, max=(2**32)-1)) for i in range(2)]
        alu_out = Signal(intbv(0, min=0, max=(2**32)-1))
        alu = ALU(alu_a, alu_b, alu_ctrl_pin, alu_out)
        if ctrl_int_signals[1] == 1:
            alu_a.next = pc_out
        elif ctrl_int_signals[1] == 2:
            alu_a.next = pc4_out
        else:
            alu_a.next = reg_read_data1

        if ctrl_int_signals[2] == 0 and ctrl_bool_signals[5] == True:
            alu_b.next = imms[4]
        elif ctrl_int_signals[2] == 1  and ctrl_bool_signals[5] == True:
            alu_b.next = imms[0]
        elif ctrl_int_signals[2] == 2 and ctrl_bool_signals[5] == True:
            alu_b.next = imms[3]
        else:
            alu_b.next = reg_read_data2

        

        jalr_out = Signal(intbv(0, min=0, max=(2**32)-1))
        jalr = JalrTarget(reg_read_data1, imms[4], jalr_out)

        if ctrl_int_signals[3] == 3:
            pc_in.next = jalr_out
        elif ctrl_int_signals[3] == 1 and ctrl_bool_signals[0] == True:
            pc_in.next = imms[1]
        elif ctrl_int_signals[3] == 2:
            pc_in.next = imms[2]
        else:
            pc_in.next = pc4_out

        data_mem_out = Signal(intbv(0, min=0, max=(2**32)-1))
        d_mem = DataMemory(clk, alu_out[9:2], reg_read_data2, data_mem_out, not ctrl_bool_signals[2], ctrl_bool_signals[2])

        if ctrl_bool_signals[4] == True:
            reg_write_data.next = data_mem_out
        else:
            reg_write_data.next = alu_out

    return top

@block
def Simulate():
    clk = Signal(bool(0))
    # reset_n = Signal(bool(1))
    reset_n = ResetSignal(0, active=0, isasync=False)
    core = Core(clk, reset_n)
    @instance
    def clockGen():
        c = 0
        while c <= 100:
            clk.next = not clk
            c+=1
            yield delay(10)

    @instance
    def stimulus():
        yield delay(10)
        reset_n.next = 1

    return stimulus, clockGen, core

ACTIVE_LOW, INACTIVE_HIGH = 0, 1

tb = Simulate()
tb.config_sim(trace=True)
tb.run_sim()