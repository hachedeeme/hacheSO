## Policy
##
## + choose_pcb(queue): choose a pcb from queue.

class Policy:
    
    def __init__(self):
        self.quantum = 1
        self.clock_pulses = 0
        
    def choose_pcb(self, queue):
        raise NotImplementedError("Please Implement this method")
    
    def is_finish(self):
        return self.quantum == self.clock_pulses
        
    def raise_clock_pulses(self):
        self.clock_pulses += 1
        
    def reset_clock_pulses(self):
        self.clock_pulses = 0