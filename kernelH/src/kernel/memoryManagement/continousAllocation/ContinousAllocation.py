from src.kernel.memoryManagement.MemoryManagementUnit import MemoryManagementUnit

class ContinousAllocation(MemoryManagementUnit):

    def __init__(self, memory, fit_strategy):
        MemoryManagementUnit.__init__(self, memory)
        self.fit = fit_strategy
    
    def load(self, program):
        pass