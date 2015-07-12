import unittest

from src.kernel.memoryManagement.MemoryManagementUnit import MemoryManagementUnit
from src.hardware.Memory import Memory
from src.process.instructions.Add import Add
from src.process.Program import Program

class TestMemoryManagementUnit(unittest.TestCase):
    def setUp(self):
        self.inst1 = Add(1,1)
        self.inst2 = Add(2,1)
        self.inst3 = Add(3,1)
        self.program = Program('Program 1')
        self.program.add_instruction(self.inst1)
        self.program.add_instruction(self.inst2)
        self.program.add_instruction(self.inst3)
        
        # Memory
        self.memory = Memory(1024)
        self.memory.load(self.program)
        
        self.mmu = MemoryManagementUnit(self.memory)
    
    def test_creation(self):
        pass
        
    def test_fetch_instruction(self):
        instruction = self.mmu.fetch_instruction(0)
        self.assertEqual(instruction, self.inst1)
        
if __name__ == '__main__':
    unittest.main()