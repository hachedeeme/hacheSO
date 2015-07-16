from PcbState import New

class Pcb:
    def __init__(self, process_id, program_counter, displacement):
        self.pid   = process_id
        self.pc    = program_counter
        self.state = New()
        self.program_length = displacement
        self.base_direction = program_counter

    def change_state(self, new_state):
        self.state = new_state
        
    def raise_pc(self):
        self.pc += 1
        
    def is_finish(self):
        return self.pc == (self.base_direction + self.program_length)
    
    def last_dir(self):
        return self.base_direction + self.program_length - 1