import unittest

from src.hardware.Memory import Memory
from src.memoryManagement.continousAllocation.ContinousAllocation import ContinousAllocation
from src.memoryManagement.continousAllocation.Fits import FirstFit
from src.process.Pcb import Pcb
from src.process.Program import Program
from src.process.instructions.Add import Add


class TestContinousAllocation(unittest.TestCase):
    def setUp(self):
        self.program1 = Program('p1')
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        
        self.program2 = Program('p2')
        self.program2.add_instruction(Add(2, 1))
        self.program2.add_instruction(Add(2, 1))
        
        self.program3 = Program('p3')
        self.program3.add_instruction(Add(3, 1))
        self.program3.add_instruction(Add(3, 1))
        self.program3.add_instruction(Add(3, 1))
        
        self.program4 = Program('p4')
        self.program4.add_instruction(Add(4, 1))
        self.program4.add_instruction(Add(4, 1))
        self.program4.add_instruction(Add(4, 1))
        self.program4.add_instruction(Add(4, 1))
        
        # Memory
        self.memory = Memory(1024)
        
        self.mmu = ContinousAllocation(self.memory, FirstFit())
    
    def test_load_a_program(self):
        program1_base = self.mmu.load(self.program1)
        
        self.assertEqual(len(self.mmu.fit.free_blocks),1)
        self.assertEqual(self.mmu.fit.free_blocks[0].base,8)
        self.assertEqual(self.mmu.fit.free_blocks[0].limit,1016)
        
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 1)
        
        self.mmu.load(self.program2)
        self.assertEqual(len(self.mmu.fit.free_blocks),1)
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 2)
        
        program3_base = self.mmu.load(self.program3)
        self.assertEqual(len(self.mmu.fit.free_blocks),1)
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 3)
        
        self.mmu.load(self.program4)
        self.assertEqual(len(self.mmu.fit.free_blocks),1)
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 4)
        
        # Free the program 1.
        self.mmu.free(Pcb(0, program1_base, self.program1.length()))
        self.assertEqual(len(self.mmu.fit.free_blocks),2)
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 3)
        
        # Free the program 3.
        self.mmu.free(Pcb(0, program3_base, self.program3.length()))
        self.assertEqual(len(self.mmu.fit.free_blocks),3)
        self.assertEqual(len(self.mmu.fit.assigned_blocks), 2)
        
        
    def test_fetch_instruction(self):
        instruction = self.mmu.fetch_instruction(0)
        self.assertEqual(instruction, None)
        
if __name__ == '__main__':
    unittest.main()