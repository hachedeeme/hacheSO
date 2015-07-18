from Page import Page


class PageTable():
    def __init__(self, page_size):
        self.page_size = page_size
        self.assigned_pages = {}
        self.free_pages     = []
        
    def add_unit(self, pid, page_table_unit):
        self.assigned_pages[pid] = page_table_unit
        
    def get_unit(self, pid):
        return self.assigned_pages[pid]
    
    def add_free_pages(self, pages):
        self.free_pages += pages
    
    def init_free_pages(self, memory):
        self.free_pages = self.get_free_pages(memory)
        
    def get_current_instruction(self, memory, pcb_id, program_counter):
        current_unit = self.assigned_pages[pcb_id]
        return memory.read(current_unit.get_physical_direction(program_counter))
        
    def get_free_pages(self, memory):
        pages_counter = 0
        base_dir      = 0
        free_pages    = []
        memory_size   = memory.size
        
        while memory_size > 0:
            free_pages.append(Page(pages_counter, base_dir, self.page_size))
            pages_counter += 1
            base_dir    += self.page_size
            memory_size -= self.page_size
        
        return free_pages
    
    def take_n_pages(self, n):
        pages = []
        if n <= len(self.free_pages):
            for _ in range(0,n):
                pages.append(self.free_pages.pop(0))
        return pages