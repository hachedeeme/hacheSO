import unittest

from src.hardware.Cpu import Cpu
from src.hardware.HardDisk import HardDisk
from src.hardware.Memory import Memory
from src.kernel.Kernel    import Kernel
from src.memoryManagement.MemoryManagementUnit import MemoryManagementUnit
from src.process.Program import Program
from src.process.instructions.Print import Print


class TestKernel(unittest.TestCase):
    def setUp(self):
        memory    = Memory(1024)
        mmu = MemoryManagementUnit(memory)
        hard_disk = HardDisk()
        cpu = Cpu(None, None, None)
        
        self.kernel = Kernel(cpu, mmu, hard_disk)
        self.program1 = Program('program1')
        self.program1.add_instruction(Print("Hello ", self.kernel.console))
        self.program1.add_instruction(Print("how ", self.kernel.console))
        self.program1.add_instruction(Print("are  ", self.kernel.console))
        self.program1.add_instruction(Print("you?", self.kernel.console))
        self.kernel.save_program(self.program1)
        
    def test_creat_pcb_when_all_is_fine(self):
        new_pcb = self.kernel.create_pcb_of(self.program1)
        self.assertEqual(self.kernel.pids, 1)
        self.assertEqual(self.kernel.mmu.used_space(), new_pcb.program_length)
        self.assertEqual(new_pcb.pc, 0)
        
        new_pcb = self.kernel.create_pcb_of(self.program1)
        self.assertEqual(self.kernel.pids, 2)
        self.assertEqual(self.kernel.mmu.used_space(), new_pcb.program_length*2)
        self.assertEqual(new_pcb.pc, 4)
        
if __name__ == '__main__':
    unittest.main()