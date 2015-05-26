## Fifo
##
## + choose_pcb(queue): choose a pcb from queue.

from src.scheduling.policies.Policy import Policy

class Fifo(Policy):
    def choose_pcb(self, queue):
        return queue.get()