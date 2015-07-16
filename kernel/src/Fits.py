from Block import Block

class FirstFit():
    def __init__(self):
        self.free_blocks     = []
        self.assigned_blocks = []
        
    # Returns the first block that satisfies, if none returns None.
    def choose_free_block(self, limit):
        for block_index in range(len(self.free_blocks)):
            if self.free_blocks[block_index].satisfy(limit):
                return self.free_blocks.pop(block_index)
        return None
    
    def get_assigned_block_by_base_dir(self, base):
        for block in self.assigned_blocks:
            if block.base == base:
                return block
        return None
    
    def get_sorted_assigned_blocks(self):
        a = [] + self.assigned_blocks
        return sorted(a, key=get_base)
    
    def remove_assigned_block(self, block):
        self.assigned_blocks.remove(block)
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = self.get_free_blocks(memory)
    
    def add_free_block(self, a_block):
        self.free_blocks.append(a_block)
    
    def add_assinged_block(self, a_block):
        self.assigned_blocks.append(a_block)
        
    def get_free_blocks(self, memory):
        free_blocks   = []
        base_dir      = 0
        limit_counter = 0
        count = False
        
        for index_dir in range(0, memory.size):
            if count:
                if memory.is_use_direction(index_dir):
                    free_blocks.append(Block(base_dir, limit_counter))
                    base_dir = 0
                    limit_counter = 0
                    count = False
                else:
                    limit_counter += 1
                    
            elif not memory.is_use_direction(index_dir):
                count = True
                base_dir = index_dir
                limit_counter = 1
        # The last block.
        if count:
            free_blocks.append(Block(base_dir, limit_counter))
        
        return free_blocks  
    
# =========================================================================        
class BestFit(FirstFit):
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = sorted(self.get_free_blocks(memory), key=get_limit)
        
    def add_free_block(self, a_block):
        blocks = add_in_order(self.free_blocks, a_block, lambda x,y: x <= y)
        self.free_blocks = blocks

# =========================================================================        
class WorstFit(FirstFit):
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = sorted(self.get_free_blocks(memory), key=get_limit, reverse=True)
    
    def add_free_block(self, a_block):
        blocks = add_in_order(self.free_blocks, a_block, lambda x,y: x >= y)
        self.free_blocks = blocks
        
# ============= #
# === UTILS === #
# ============= #
def get_limit(a_block):
    return a_block.limit

def get_base(a_block):
    return a_block.base
    
def add_in_order(blocks, a_block, criteria_function):
    if not blocks:
        return [a_block]
    elif criteria_function(a_block.limit, blocks[0].limit):
        return [a_block] + blocks
    else:
        return [blocks.pop(0)] + add_in_order(blocks, a_block, criteria_function)
