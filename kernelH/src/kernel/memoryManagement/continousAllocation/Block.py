
class Block():
    def __init__(self, base, limit):
        self.base  = base
        self.limit = limit
        self.free  = True
        
    def is_free(self):
        return self.free
    
    def belongs(self, mem_dir):
        return mem_dir in range(self.base, self.last_dir())
    
    def last_dir(self):
        return self.base + self.limit - 1 