## LongTermScheduler
## - ready_queue(Queue(Pcb))..: Queue of the system's Pcbs.
## - new_processes([Pcb]).....: List of the news processes.
##
## + add_new_process(Pcb)..: Add a new Pcb to the list of processes.
## + choose_new_process()..: Choose a Pcb from the ready Queue.

from src.scheduling.Scheduler import Scheduler

class LongTermScheduler(Scheduler):
    
    def __init__(self, queue):
        super().__init__(queue)
        self.new_processes = []

    def add_new_process(self, a_pcb):
        self.new_processes.append(a_pcb)

    def choose_new_process(self):
        # This method chose only the firs pcb
        if self.new_processes:
            self.queue.put(self.new_processes[0])
    