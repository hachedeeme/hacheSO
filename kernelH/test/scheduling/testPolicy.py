import unittest
import queue

from src.process.Pcb import Pcb
from src.scheduling.policies.Fifo import Fifo

class TestPolicy(unittest.TestCase):
    def setUp(self):
        # Empty queue
        self.queue = queue.Queue()
        self.queue.put(Pcb(1,1,3))
        self.queue.put(Pcb(2,3,2))
        self.queue.put(Pcb(3,5,1))
        
        ### Policies ###
        # First In First Out
        self.fifo = Fifo()
        
    def test_choose_process_for_fifo(self):
        self.assertEquals(self.fifo.choose_pcb(self.queue).pid, 1)
        self.assertEquals(self.fifo.choose_pcb(self.queue).pid, 2)
        
if __name__ == '__main__':
    unittest.main()