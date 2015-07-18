
class PageTableUnit():
    def __init__(self, page_size, pages):
        self.page_size = page_size
        self.pages     = pages
        
    def get_physical_direction(self, logical_direction):
        # Take the page index
        page_index   = int(logical_direction / self.page_size)
        
        # Take the displacement
        displacement = logical_direction % self.page_size
        
        return self.pages[page_index].base + displacement