from myhdl import *

from Core.ControlDecode import AluOp

@block
def AluControl(AluOp, Func3, Func7, AluCtrl):


    always_comb
    def comb():
        AluCtrl.next = 0

        if AluOp == 0:
            AluCtrl.next = concat(intbv(0, min=0, max=1),Func7, Func3)      # R

        elif AluOp == 1:
            if Func3 == 1:
                AluCtrl.next = concat(intbv(0,min=0, max=1), Func7, Func3)
            else:
                AluCtrl.next = concat(intbv(0, min=0, max=(2**2)-1), Func3)

        elif AluOp == 2:
            AluCtrl.next = concat(intbv(2, min=0, max=(2**2)-1), Func3)     # SB
        
        elif AluOp == 3:
            AluCtrl.next = intbv((2**5)-1, min=0, max=(2**5)-1)             # Jal, Jalr

        elif AluOp in (4,5,6):
            AluCtrl.next = intbv(0, min=0, max= (2**5)-1)                   # Load / Store / LUI

    return comb()
        
AluOp = Signal(intbv(0, min=0, max=3))
Func3 = Signal(intbv(0, min=0, max=3))
Func7 = Signal(intbv(0, min=0, max=7))
AluCtrl = Signal(intbv(0, min=0, max=(2**5)-1))

aluctrl = AluControl(AluOp, Func3, Func7, AluCtrl)
aluctrl.convert(hdl='Verilog')