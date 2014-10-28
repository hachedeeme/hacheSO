from Memory import Memory
from Disk import Disk
from Program import Program

class DeviceManager:
	
	def __init__(self):
		self.memory = Memory()
		self.disk = Disk()

	def save_program(self, program):
		self.disk.add_program(program)

	def get_program(self, programs_name):
		return self.disk.get_program(programs_name)