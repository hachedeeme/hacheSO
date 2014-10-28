class Program:
    def __init__(self, programs_name):
    	self.name = programs_name
    	self.instructions = []
    	
    def add_instruction(self, instruction):
        self.instructions.append(instruction)
