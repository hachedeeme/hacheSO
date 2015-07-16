## Fifo
##
## + choose_pcb(queue): choose a pcb from queue.

from Policy import Policy

class Fifo(Policy):
    
    def __init__(self):
        Policy.__init__(self)
    
    def choose_pcb(self, queue):
        if not queue.empty():
            return queue.get()