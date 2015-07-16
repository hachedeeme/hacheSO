from MemoryManagementUnit import MemoryManagementUnit

class Paging(MemoryManagementUnit):
    
    def __init__(self, memory, page_table):
        MemoryManagementUnit.__init__(self, memory)
        self.page_table = page_table