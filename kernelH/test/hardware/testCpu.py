#import time
import queue
import unittest

from src.hardware.Cpu import Cpu
from src.hardware.Memory import Memory
from src.kernel.MemoryManagementUnit import MemoryManagementUnit
from src.process.Program import Program
from src.process.instructions.Add import Add
from src.scheduling.ShortTermScheduler import ShortTermScheduler
from src.scheduling.policies.RoundRobin import RoundRobin
from src.process.Pcb import Pcb


class TestClock(unittest.TestCase):
    def setUp(self):
        
        # Programs
        self.program1 = Program('p1')
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        
        self.program2 = Program('p2')
        self.program2.add_instruction(Add(1, 1))
        
        self.queue = queue.Queue()
        self.scheduler = ShortTermScheduler(self.queue, RoundRobin(3))
        self.mmu = MemoryManagementUnit(Memory(1024))
        
        
        self.cpu = Cpu(self.scheduler, self.mmu, None)
        
        self.queue.put(Pcb(1, self.mmu.load(self.program1), self.program1.length()))
        self.queue.put(Pcb(2, self.mmu.load(self.program2), self.program2.length()))
        
        
    def test_set_new_pcb(self):
        self.assertEqual(self.queue.qsize(), 2)
        self.cpu.set_new_pcb()
        self.assertEqual(self.queue.qsize(), 1)
        self.assertEqual(self.cpu.current_pcb_tuple.pid, 1)
                
if __name__ == '__main__':
    unittest.main()