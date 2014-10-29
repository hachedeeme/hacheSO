from Instruction import Instruction


class Add(Instruction):
    def __init__(self, num1, num2):
        self.op1 = num1
        self.op2 = num2

    def execute(self):
        return self.op1 + self.op2
