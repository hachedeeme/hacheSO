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
        
        #Pcbs
        self.pcb_id0 = Pcb(0,0,0)
        self.pcb_id1 = Pcb(1,0,0)
        
    def test_creation(self):
        self.assertEqual(self.scheduler.queue, self.queue)
        self.assertEqual(self.scheduler.new_processes, [])
        self.assertEqual(self.scheduler.finished_processes, [])
        
    def test_add_new_process(self):
        # Add a new Pcb with id 0.
        self.scheduler.add_new_process(self.pcb_id0)
        
        # The size of new process list should be 1.
        self.assertEquals(len(self.scheduler.new_processes), 1)
        
        # The fist element of the new processes list should be pcb_id0
        self.assertEquals(self.scheduler.new_processes[0], self.pcb_id0)
        
        # Add a another Pcb with id 1.
        self.scheduler.add_new_process(self.pcb_id1)
        
        # The size of new process list should be 2.
        self.assertEquals(len(self.scheduler.new_processes), 2)
        
        # The second element of the new processes list should be pcb_id1
        self.assertEquals(self.scheduler.new_processes[1], self.pcb_id1)

    def test_choose_new_process_with_one_pcb(self):
        # the new processes list is empty.
        self.assertEqual(self.scheduler.new_processes, [])
        
        # choose a new pcb.
        new_pcb = self.scheduler.choose_new_process()
        
        # the new pcb should be None.
        self.assertEqual(new_pcb, None)

        # Add a new Pcb with id 0.
        self.scheduler.add_new_process(self.pcb_id0)
        
        # choose a new pcb.
        new_pcb = self.scheduler.choose_new_process()
        
        # the new pcb should be pcb_id0.
        self.assertEquals(new_pcb, self.pcb_id0)
        
        # the new processes list should be empty.
        self.assertEqual(self.scheduler.new_processes, [])
        
    def test_choose_new_process_with_more_of_one_pcbs(self):
        # the new processes list is empty.
        self.assertEqual(self.scheduler.new_processes, [])
        
        # choose a new pcb.
        new_pcb = self.scheduler.choose_new_process()
        
        # the new pcb should be None.
        self.assertEqual(new_pcb, None)

        # Add a new Pcb with id 1.
        self.scheduler.add_new_process(self.pcb_id1)
        # Add a new Pcb with id 0.
        self.scheduler.add_new_process(self.pcb_id0)
        
        # choose a new pcb.
        new_pcb = self.scheduler.choose_new_process()
        
        # the new pcb should be pcb_id1.
        self.assertEquals(new_pcb, self.pcb_id1)
        
        # the new processes list should content one pcb.
        self.assertEqual(len(self.scheduler.new_processes), 1)
        
    def test_put_new_process_in_ready(self):
        # Add a new Pcb with id 1.
        self.scheduler.add_new_process(self.pcb_id1)
        # Add a new Pcb with id 0.
        self.scheduler.add_new_process(self.pcb_id0)
        
        # Put pcb_id1 in the first place to the ready queue
        self.scheduler.put_new_process_in_ready()
        # Put pcb_id0 in the second place to the ready queue
        self.scheduler.put_new_process_in_ready()
        
        # The fist element of the ready queue should be pcb_id1
        self.assertEqual(self.queue.get(), self.pcb_id1)        
        # The second element of the ready queue should be pcb_id0
        self.assertEqual(self.queue.get(), self.pcb_id0)
        
        # The new processes list should be empty.
        self.assertEqual(self.scheduler.new_processes, [])
        
if __name__ == '__main__':
    unittest.main()