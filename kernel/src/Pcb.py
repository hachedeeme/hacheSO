from PcbState import *


class Pcb:
    def __init__(self, pid, pc, displacement):
        self.pid = pid
        self.state = New()
        self.pc = pc
        self.program_length = displacement
        self.base_direction = pc

    def set_state(self, state):
        self.state = state