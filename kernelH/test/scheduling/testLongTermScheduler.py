import unittest
import queue

from src.scheduling.LongTermScheduler import LongTermScheduler
from src.process.Pcb import Pcb

class TestLongTermScheduler(unittest.TestCase):
    def setUp(self):
        # Empty queue
        self.queue = queue.Queue()
        # Long Term Scheduler
        self.scheduler = LongTermScheduler(self.queue)
                
    def test_add_new_process(self):
        # Add a new Pcb
        self.scheduler.add_new_process(Pcb(0,0,0))
        # The size of new process list should be 1.
        self.assertEquals(len(self.scheduler.new_processes), 1)
        # Add a another Pcb.
        self.scheduler.add_new_process(Pcb(1,0,0))
        # The size of new process list should be 1.
        self.assertEquals(len(self.scheduler.new_processes), 2)

    def test_choose_new_process(self):
        # Add a new pcb with process id 1.
        self.scheduler.add_new_process(Pcb(1,0,0))
        # Add a new pcb with process id 0.
        self.scheduler.add_new_process(Pcb(0,0,0))
        # When choose a new process.
        self.scheduler.put_new_process()
        # The process id of the first pcb should be 1.
        self.assertEquals(self.scheduler.queue.get().pid, 0)
        
if __name__ == '__main__':
    unittest.main()