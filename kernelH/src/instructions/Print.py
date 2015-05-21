from src.instructions.Instruction import Instruction

class Print(Instruction):
    def __init__(self, objToPrint, console):
        self.message = str(objToPrint)
        self.console = console

    def execute(self):
        self.console.printMessage(self.message)
