

class MemoryManagementUnit():

    def __init__(self, memory):
        self.memory = memory
        
    def fetch_instruction(self, dir_mem):
        return self.memory.read(dir_mem)