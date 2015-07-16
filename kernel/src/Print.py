## Print
## - message(String)...: Program's name.
## - console(Console)..: The console where the instruction will be printed.
##
## + execute().........: execute the instruction.

from IOInstruction import IOInstruction

class Print(IOInstruction):
    def __init__(self, objToPrint, console):
        self.message = str(objToPrint)
        self.console = console

    def execute(self):
        self.console.printMessage(self.message)
        
    def __str__(self):
        return 'Print("%s")' % (self.message)
