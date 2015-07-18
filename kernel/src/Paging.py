from MemoryManagementUnit import MemoryManagementUnit
from PageTable import PageTable
from PageTableUnit import PageTableUnit

class Paging(MemoryManagementUnit):
    
    def __init__(self, memory, page_size):
        MemoryManagementUnit.__init__(self, memory)
        self.page_size  = page_size
        self.page_table = PageTable(self.page_size)
        self.page_table.init_free_pages(self.memory)
        
    def fetch_instruction(self, pcb_id, program_counter):
        return self.page_table.get_current_instruction(self.memory, pcb_id, program_counter)
    
    def load(self, program, pid=0):
        number_of_pages = self.get_number_of_pages(program)
        pages = self.page_table.take_n_pages(number_of_pages)
        
        if pages:
            self.page_table.add_unit(pid, PageTableUnit(self.page_size, pages))
            self.load_program_to_pages(program, pages)
        
        # 0 is the base dir for a new pcb in paging.
        return 0
            
    def free(self, a_pcb):
        unit = self.page_table.get_unit(a_pcb.pid)
        
        for page in unit.pages:
            self.memory.free(page.base, page.limit)
        
        self.page_table.add_free_pages(unit.pages)
        
    def get_number_of_pages(self, program):
        number_of_pages = int(program.length() / self.page_size)
        if program.length() % self.page_size > 0: 
            number_of_pages += 1
        return number_of_pages
    
    def load_program_to_pages(self, program, pages):
        instruction_index = 0
        for page in  pages:
            current_dir = page.base
            for _ in range(0, self.page_size):
                if instruction_index >= program.length():
                    break
                else:
                    self.memory.write(current_dir, program.instructions[instruction_index])
                    instruction_index += 1
                    current_dir  += 1