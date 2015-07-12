from src.memoryManagement.MemoryManagementUnit import MemoryManagementUnit

class ContinousAllocation(MemoryManagementUnit):

    def __init__(self, memory, fit_strategy):
        MemoryManagementUnit.__init__(self, memory)
        self.fit = fit_strategy
        self.fit.init_free_blocks_of(self.memory)
    
    def load(self, program):
        free_block    = self.fit.choose_free_block(program.length())
        assigne_block = self.memory.load(program, free_block)
        