from src.process.PcbState import New

class Pcb:
    def __init__(self, process_id, program_counter, displacement):
        self.pid   = process_id
        self.pc    = program_counter
        self.state = New()
        self.program_length = displacement
        self.base_direction = program_counter

    def change_state(self, new_state):
        self.state = new_state