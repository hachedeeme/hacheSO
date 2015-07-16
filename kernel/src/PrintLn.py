## PrintLn
## - message(String)...: Program's name.
## - console(Console)..: The console where the instruction will be printed.
##
## + execute().........: execute the instruction.

from Print import Print

class PrintLn(Print):
    
    def execute(self):
        self.console.printLn(self.message)

    def __str__(self):
        return 'PrintLn("%s")' % (self.message)