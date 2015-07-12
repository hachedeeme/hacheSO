
class Fit():
    def __init__(self):
        self.free_blocks     = []
        self.assigned_blocks = []
        
    def choose_free_block(self):
        raise NotImplementedError("Please Implement this method")
    
    def init_free_blocks_of(self, memory):
        pass
    
    def add_free_block(self, a_block):
        self.free_blocks.append(a_block)
    
    def add_assinged_block(self, a_block):
        self.assigned_blocks.append(a_block)