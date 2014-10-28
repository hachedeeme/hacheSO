class Pcb:
	def __init__(self, pid, pc):
		self.pid = pid
		self.state = 'NEW'
		self.pc = pc
		self.program_length = 1
		self.base_direction = 0

	def set_state(self, state):
		self.state = state