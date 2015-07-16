

from Disk import Disk
from Memory import Memory
class DeviceManager:
    def __init__(self):
        self.memory = Memory()
        self.disk = Disk()

    def save_program(self, program):
        self.disk.add_program(program)

    def get_program(self, programs_name):
        return self.disk.get_program(programs_name)

    def load_program(self, program):
        return self.memory.load(program)
