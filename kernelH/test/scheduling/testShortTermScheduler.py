import queue
import unittest

from src.process.Pcb import Pcb
from src.scheduling.ShortTermScheduler import ShortTermScheduler
from src.scheduling.policies.Fifo import Fifo


class TestShortTermScheduler(unittest.TestCase):
    def setUp(self):
        # Empty queue
        self.queue = queue.Queue()
        # Short Term Scheduler
        self.scheduler = ShortTermScheduler(self.queue, Fifo())

    def test_choose_new_process(self):
        # Add a new pcb with process id 1.
        self.queue.put(Pcb(1,0,0))
        # The process id of the first pcb should be 1.
        self.assertEquals(self.scheduler.choose_new_process().pid, 1)
        
if __name__ == '__main__':
    unittest.main()