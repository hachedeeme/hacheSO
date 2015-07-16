## Program
## - name(String).................: Program's name.
## - instructions([Instruction])..: Instructions list.
##
## + add_instruction(Instruction).: Add an instruction to the instructions list.
## + length().....................: returns the instructions amount of the program.

class Program:
    def __init__(self, programs_name):
        self.name = programs_name
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def length(self):
        return len(self.instructions)
