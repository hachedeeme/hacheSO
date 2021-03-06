## Add
## - firstOp(Integer)...: The first operand of the Add instruction.
## - secondOp(Integer)..: The second operand of the Add instruction.
##
## + execute()..........: execute the instruction.

from Instruction import Instruction

class Add(Instruction):
    def __init__(self, num1, num2):
        self.firstOp  = num1
        self.secondOp = num2

    def execute(self):
        return self.firstOp + self.secondOp
    
    def __str__(self):
        return "Add(%s,%s)" % (self.firstOp, self.secondOp)
