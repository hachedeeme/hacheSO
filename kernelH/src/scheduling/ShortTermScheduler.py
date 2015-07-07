## ShortTermScheduler
## - ready_queue(Queue(Pcb))..: Queue of the system's Pcbs.
##
## + choose_new_process()..: Choose a Pcb from the ready Queue.

from src.scheduling.Scheduler import Scheduler

class ShortTermScheduler(Scheduler):
    def __init__(self, queue, policy):
        Scheduler.__init__(self, queue)
        self.policy = policy
    
    def choose_new_process(self):
        return self.policy.choose_pcb(self.queue)
    
    def is_time_out(self):
        return self.policy.is_finish()
    
    def reset_quantum(self):
        self.policy.reset_clock_pulses()
        
    def put_pcb(self, pcb):
        self.queue.put(pcb)
        
    def raise_clock_pulses(self):
        self.policy.raise_clock_pulses()