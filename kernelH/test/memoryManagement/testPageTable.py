import unittest

from src.hardware.Memory import Memory
from src.memoryManagement.continousAllocation.Page import Page
from src.memoryManagement.paging.PageTable import PageTable
from src.memoryManagement.paging.PageTableUnit import PageTableUnit


class TestPageTable(unittest.TestCase):
    
    def setUp(self):
        self.memory = Memory(32)
        self.page_table = PageTable(4)
        self.page_table.init_free_pages(self.memory)

    def test_get_free_pages(self):
        free_pages = self.page_table.get_free_pages(Memory(16))
        
        # The free pages list should have 4 pages.
        self.assertEqual(len(free_pages), 4)
        
        # The page in the 0 position should have id_num = 0, base = 0 and limit = 4.
        self.assertEqual(free_pages[0].id_num, 0)       
        self.assertEqual(free_pages[0].base,   0)       
        self.assertEqual(free_pages[0].limit,  4)       
        
        # The page in the 1 position should have id_num = 1, base = 4 and limit = 4.
        self.assertEqual(free_pages[1].id_num, 1)       
        self.assertEqual(free_pages[1].base,   4)       
        self.assertEqual(free_pages[1].limit,  4)       
        
        # The page in the 2 position should have id_num = 2, base = 8 and limit = 4.
        self.assertEqual(free_pages[2].id_num, 2)       
        self.assertEqual(free_pages[2].base,   8)       
        self.assertEqual(free_pages[2].limit,  4)       
        
        # The page in the 3 position should have id_num = 3, base = 12 and limit = 4.
        self.assertEqual(free_pages[3].id_num, 3)       
        self.assertEqual(free_pages[3].base,  12)       
        self.assertEqual(free_pages[3].limit,  4)       
        
    def test_take_n_pages(self):
        # The free pages list should have 8 pages.
        self.assertEqual(len(self.page_table.free_pages), 8)
        
        # Take 3 pages.
        pages = self.page_table.take_n_pages(3)
        
        # The page in the 0 position should have id_num = 0, base = 0 and limit = 4.
        self.assertEqual(pages[0].id_num, 0)       
        self.assertEqual(pages[0].base,   0)       
        self.assertEqual(pages[0].limit,  4)       
        
        # The page in the 1 position should have id_num = 1, base = 4 and limit = 4.
        self.assertEqual(pages[1].id_num, 1)       
        self.assertEqual(pages[1].base,   4)       
        self.assertEqual(pages[1].limit,  4)       
        
        # The page in the 2 position should have id_num = 2, base = 8 and limit = 4.
        self.assertEqual(pages[2].id_num, 2)       
        self.assertEqual(pages[2].base,   8)       
        self.assertEqual(pages[2].limit,  4)   
        
        # The pages list should have 3 pages.
        self.assertEqual(len(pages), 3)

        # The free pages list should have 5 pages.
        self.assertEqual(len(self.page_table.free_pages), 5)
        
        # Take 5 pages.
        pages = self.page_table.take_n_pages(5)
        
        # The pages list should have 5 pages.
        self.assertEqual(len(pages), 5)
        
        # The free pages list should have 0 pages.
        self.assertEqual(len(self.page_table.free_pages), 0)
        
        # Take 5 pages again.
        pages = self.page_table.take_n_pages(5)
        
        # The pages list should have 0 pages.
        self.assertEqual(len(pages), 0)
        
    def test_get_current_instruction(self):
        self.memory.write(0, 1)
        self.memory.write(1, 2)
        self.memory.write(2, 3)
        self.memory.write(3, 4)
        
        self.memory.write(8, 5)
        self.memory.write(9, 6)

        self.page_table.add_unit(0, PageTableUnit(4, [Page(0,0,4), Page(0,8,4)]))
        
        self.assertEqual(self.page_table.get_current_instruction(self.memory, 0, 5), 6)
        self.assertEqual(self.page_table.get_current_instruction(self.memory, 0, 0), 1)
        
        
        
if __name__ == "__main__":
    unittest.main()