import unittest

from src.hardware.Memory import Memory
from src.memoryManagement.continousAllocation.Page import Page
from src.memoryManagement.paging.Paging import Paging
from src.process.Pcb import Pcb
from src.process.Program import Program


class TestPaging(unittest.TestCase):
    
    def setUp(self):
        self.memory = Memory(16)
        self.paging = Paging(self.memory, 4)

    def test_get_number_of_pages(self):
        program = Program("")
        program.add_instruction(1)
        
        self.assertEqual(self.paging.get_number_of_pages(program), 1)

        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        
        self.assertEqual(self.paging.get_number_of_pages(program), 1)
        
        program.add_instruction(1)

        self.assertEqual(self.paging.get_number_of_pages(program), 2)
        
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        
        self.assertEqual(self.paging.get_number_of_pages(program), 3)
        
    def test_load_program_to_pages(self):
        program = Program("")
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(2)
        
        pages = [Page(0,0,4), Page(1,8,4)]
        
        self.paging.load_program_to_pages(program, pages)
        
        for mem_dir in range(0,4):
            self.assertEqual(self.memory.read(mem_dir), 1)
            
        self.assertEqual(self.memory.read(8), 2)
        
        self.assertEqual(self.memory.used_space(), 5)
        
    def test_load(self):
        program = Program("")
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        
        self.paging.load(program, 0)
        
        for mem_dir in range(0,5):
            self.assertEqual(self.memory.read(mem_dir), 1)
            
        self.assertTrue(self.paging.page_table.assigned_pages[0] != None)
        
    def test_free(self):
        program = Program("")
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        program.add_instruction(1)
        
        self.paging.load(program, 0)
        self.assertEqual(self.memory.used_space(), 6)
        
        self.paging.free(Pcb(0, 0, program.length()))
        self.assertEqual(self.memory.used_space(), 0)
        
        
if __name__ == "__main__":
    unittest.main()