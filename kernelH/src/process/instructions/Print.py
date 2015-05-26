## Print
## - message(String)...: Program's name.
## - console(Console)..: The console where the instruction will be printed.
##
## + execute().........: execute the instruction.

from src.process.instructions.Instruction import Instruction

class Print(Instruction):
    def __init__(self, objToPrint, console):
        self.message = str(objToPrint)
        self.console = console

    def execute(self):
        self.console.printMessage(self.message)
