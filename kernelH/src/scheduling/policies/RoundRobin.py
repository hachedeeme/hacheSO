## RoundRobin
##
## + choose_pcb(queue): choose a pcb from queue.

from src.scheduling.policies.Fifo import Fifo

class RoundRobin(Fifo):
    def __init__(self, quantum):
        super().__init__()
        self.quantum = quantum
        self.clock_pulses = 0
    
    def is_finish(self):
        return self.quantum == self.clock_pulses
        
    def raise_clock_pulses(self):
        self.clock_pulses += 1
        
    def reset_quantum(self):
        self.clock_pulses = 0