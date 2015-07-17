from src.memoryManagement.MemoryManagementUnit import MemoryManagementUnit

class Paging(MemoryManagementUnit):
    
    def __init__(self, memory, page_table, page_size):
        MemoryManagementUnit.__init__(self, memory)
        self.page_table = page_table
        
    def fetch_instruction(self, pcb_id, program_counter):
        return self.page_table.get_current_instruction(self.memory, pcb_id, program_counter)
    
    def load(self, program):
        pass
    
    def free(self, a_pcb):
        pass