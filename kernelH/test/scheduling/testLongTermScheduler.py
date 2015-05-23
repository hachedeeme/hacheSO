import unittest
import queue

from src.scheduling.LongTermScheduler import LongTermScheduler

class TestLongTermScheduler(unittest.TestCase):
    def setUp(self):
        # Empty ready queue
        self.queue = queue.Queue()
        # Long Term Scheduler
        self.scheduler = LongTermScheduler(self.queue)
                
    def test_add_new_process(self):
        # The HardDisk data is empty.
        pass

    def test_choose_new_process(self):
        # Save the program1 on the HardDisk
        pass
       
if __name__ == '__main__':
    unittest.main()