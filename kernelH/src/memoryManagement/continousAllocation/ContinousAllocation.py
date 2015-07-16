from src.kernel.Exceptions import OutOfMemory
from src.memoryManagement.MemoryManagementUnit import MemoryManagementUnit

class ContinousAllocation(MemoryManagementUnit):

    def __init__(self, memory, fit_strategy):
        MemoryManagementUnit.__init__(self, memory)
        self.fit = fit_strategy
        self.fit.init_free_blocks_of(self.memory)
    
    def load(self, program):
        # Choose a free block
        free_block    = self.fit.choose_free_block(program.length())
        
        if not free_block:
            self.compact()
            self.fit.init_free_blocks_of(self.memory)
            free_block = self.fit.choose_free_block(program.length())
            # If no have space raise an OutOfMemory exception.
            if not free_block: raise OutOfMemory()
        
        # Load the program in the chosen block and returns the assigned block.
        assigne_block = self.memory.load_program_to_block(program, free_block)
        
        # Add the assigned block in the assigned blocks list.
        self.fit.add_assinged_block(assigne_block)

        # Obtain the free blocks.        
        self.fit.init_free_blocks_of(self.memory)
        
        return assigne_block.base
    
    def free(self, a_pcb):
        # Free the program
        self.memory.free(a_pcb.base_direction, a_pcb.program_length)
        
        # Obtain the released block.
        released_block = self.fit.get_assigned_block_by_base_dir(a_pcb.base_direction)
        
        # Remove it of assigned blocks list.
        self.fit.remove_assigned_block(released_block)
        
        # Obtain the free blocks.
        self.fit.init_free_blocks_of(self.memory)
        
    def compact(self):
        # Get all assigned blocks sorted by base_dir.
        assigned_blocks = self.fit.get_sorted_assigned_blocks()
        
        for block in assigned_blocks:
            # Get the first free direction in memory.
            first_free_dir = self.memory.get_first_free_dir()
            
            if first_free_dir < block.base:
                # Move the assigned block to this direction.
                self.memory.move(block, first_free_dir)
                