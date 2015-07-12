
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
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = memory.get_free_blocks()
    
    def add_free_block(self, a_block):
        self.free_blocks.append(a_block)
    
    def add_assinged_block(self, a_block):
        self.assigned_blocks.append(a_block)
    
# =========================================================================        
class BestFit(FirstFit):
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = sorted(memory.get_free_blocks(), key=get_key)
        
    def add_free_block(self, a_block):
        blocks = add_in_order(self.free_blocks, a_block, lambda x,y: x <= y)
        self.free_blocks = blocks

# =========================================================================        
class WorstFit(FirstFit):
    
    def init_free_blocks_of(self, memory):
        self.free_blocks = sorted(memory.get_free_blocks(), key=get_key, reverse=True)
    
    def add_free_block(self, a_block):
        blocks = add_in_order(self.free_blocks, a_block, lambda x,y: x >= y)
        self.free_blocks = blocks
        
# ============= #
# === UTILS === #
# ============= #
def get_key(a_block):
    return a_block.limit
    
def add_in_order(blocks, a_block, criteria_function):
    if not blocks:
        return [a_block]
    elif criteria_function(a_block.limit, blocks[0].limit):
        return [a_block] + blocks
    else:
        return [blocks.pop(0)] + add_in_order(blocks, a_block, criteria_function)
