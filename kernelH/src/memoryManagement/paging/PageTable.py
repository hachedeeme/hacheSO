
class PageTable():
    def __init__(self):
        self.pages = {}
    
    def get_current_instruction(self, memory, pcb_id, program_counter):
        current_dir = 0
        return memory.read(current_dir)