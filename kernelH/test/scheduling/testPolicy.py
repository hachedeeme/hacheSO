import unittest
import queue

from src.process.Pcb import Pcb
from src.scheduling.policies.Fifo import Fifo

class TestPolicy(unittest.TestCase):
    def setUp(self):
        # Empty queue
        self.queue = queue.Queue()
        
        ### Policies ###
        # First In First Out
        self.fifo = Fifo()
        
    def test_choose_process(self):
        pass
        
if __name__ == '__main__':
    unittest.main()