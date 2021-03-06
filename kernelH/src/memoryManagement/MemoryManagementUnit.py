
class MemoryManagementUnit():

    def __init__(self, memory):
        self.memory = memory
        
    def fetch_instruction(self, pcb_id, dir_mem):
        return self.memory.read(dir_mem)
    
    def load(self, program, pid=0):
        return self.memory.load(program)
    
    def free(self, a_pcb):
        raise NotImplementedError("Please Implement this method")
        
    def used_space(self):
        return self.memory.used_space()