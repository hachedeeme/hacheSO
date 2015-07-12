from src.memoryManagement.MemoryManagementUnit import MemoryManagementUnit

class ContinousAllocation(MemoryManagementUnit):

    def __init__(self, memory, fit_strategy):
        MemoryManagementUnit.__init__(self, memory)
        self.fit = fit_strategy
        self.fit.init_free_blocks_of(memory)
    
    def load(self, program):
        pass