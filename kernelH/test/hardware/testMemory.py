import unittest

from src.hardware.Memory  import Memory
from src.process.Program import Program
from src.process.instructions.Add import Add

class TestMemory(unittest.TestCase):
    def setUp(self):
        # Memory
        self.memory = Memory(1024)
        
        # Programs
        self.program1 = Program('p1')
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        
        self.program2 = Program('p2')
        self.program2.add_instruction(Add(1, 1))
        
    def test_empty_memory(self):
        # The current direction of a empty memory is 0
        self.assertEqual(self.memory.current_dir, 0)
        # The memory data is empty
        self.assertEqual(len(self.memory.data), 0)

    def test_load_a_program(self):
        # Load a program in memory and save the first direction in a variable.
        first_dir = self.memory.load(self.program1)
        
        # It load 3 instructions in memory, so the current direction should be 3.
        self.assertEqual(self.memory.current_dir, 3)
        
        # The first direction should be 0.
        self.assertEqual(first_dir, 0)
        
        # The used space of the memory should be 3.
        self.assertEqual(self.memory.used_space(), 3)
        
        
        # Load a second program in memory and save the first direction in a variable.
        first_dir = self.memory.load(self.program2)
        
        # It load 1 instruction in memory, so the current direction should be 4.
        self.assertEqual(self.memory.current_dir, 4)
        
        # The first direction of the second program should be 3.
        self.assertEqual(first_dir, 3)
        
        # The used space of the memory should be 3.
        self.assertEqual(self.memory.used_space(), 4)

    def test_read_and_write_instructions(self):
        add = Add(2,2)
        # Write the instruction add in the direction 100.
        self.memory.write(100, add)
        
        # Read the memory in the direction 100 should return the add instruction.
        self.assertEqual(self.memory.read(100), add)
        
        # The used space of the memory should be 1.
        self.assertEqual(self.memory.used_space(), 1)
        
if __name__ == '__main__':
    unittest.main()