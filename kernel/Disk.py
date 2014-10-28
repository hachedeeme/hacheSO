from Program import Program

class Disk:
	def __init__(self):
		self.programs = {}

	def add_program(self, program):
		self.programs[program.name] = program

	def get_program(self, programs_name):
		return self.programs[programs_name]
