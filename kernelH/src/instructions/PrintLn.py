from src.instructions.Print import Print

class PrintLn(Print):
    
    def execute(self):
        self.console.printLn(self.message)
