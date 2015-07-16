## RoundRobin
##
## + choose_pcb(queue): choose a pcb from queue.

from Fifo import Fifo

class RoundRobin(Fifo):
    def __init__(self, quantum):
        super().__init__()
        self.quantum = quantum