import unittest

from src.kernel.Program import Program
from src.instructions.Add import Add

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.program1 = Program('Program 1')
        
    def test_creation(self):
        # The program's name should be 'Program 1'
        self.assertEqual(self.program1.name, 'Program 1')
        
        # The program's instruction list should be empty
        self.assertTrue(len(self.program1.instructions) == 0)
        
    def test_add_instruction(self):
        # Add an instruction to the program
        self.program1.add_instruction(Add(1,1))
        
        # The instructions length should be 1
        self.assertEqual(self.program1.length(), 1)
        
        # And add 3 instructions more
        self.program1.add_instruction(Add(1,1))
        self.program1.add_instruction(Add(1,1))
        self.program1.add_instruction(Add(1,1))
        
        # The instructions length should be 4
        self.assertEqual(self.program1.length(), 4)
        

if __name__ == '__main__':
    unittest.main()