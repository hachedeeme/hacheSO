import unittest
import queue

from src.process.Pcb import Pcb
from src.scheduling.policies.Fifo import Fifo
from src.scheduling.policies.RoundRobin import RoundRobin

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
        self.rr   = RoundRobin(3)
    
    ###======================###
    ### Test for FIFO policy ###    
    ###======================###
    def test_choose_process_for_fifo_when_queue_have_3_pcbs(self):
        self.assertEquals(self.fifo.choose_pcb(self.queue).pid, 1)
        self.assertEquals(self.fifo.choose_pcb(self.queue).pid, 2)
        
    def test_choose_process_for_fifo_when_queue_havent_pcbs(self):
        new_queue = queue.Queue()
        self.assertEquals(self.fifo.choose_pcb(new_queue), None)
        
    def test_raise_and_reset_clock_pulses(self):
        self.assertEquals(self.fifo.quantum, 1)
        self.assertEquals(self.fifo.clock_pulses, 0)
        self.fifo.raise_clock_pulses()
        self.assertEquals(self.fifo.clock_pulses, 1)
        self.fifo.raise_clock_pulses()
        self.assertEquals(self.fifo.clock_pulses, 2)
        self.fifo.reset_clock_pulses()
        self.assertEquals(self.fifo.clock_pulses, 0)
        
    def test_is_finish(self):
        self.assertFalse(self.fifo.is_finish())
        self.fifo.raise_clock_pulses()
        self.assertTrue(self.fifo.is_finish())
        
    ###=============================###
    ### Test for Round-Robin policy ###    
    ###=============================###
    def test_choose_process_for_round_robin(self):
        self.assertEquals(self.rr.choose_pcb(self.queue).pid, 1)
        self.assertEquals(self.rr.choose_pcb(self.queue).pid, 2)
    
    def test_is_finish_for_round_robib(self):
        self.assertFalse(self.rr.is_finish())
        self.rr.raise_clock_pulses()
        self.assertFalse(self.rr.is_finish())
        self.rr.raise_clock_pulses()
        self.assertFalse(self.rr.is_finish())
        self.rr.raise_clock_pulses()
        self.assertTrue(self.rr.is_finish())
    
        
if __name__ == '__main__':
    unittest.main()