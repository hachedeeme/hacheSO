## Policy
##
## + choose_pcb(queue): choose a pcb from queue.

class Policy:
    def choose_pcb(self, queue):
        raise NotImplementedError("Please Implement this method")

"""    def getInstructions(self, aPcb):
        return [aPcb.getCurrentIns()]"""
