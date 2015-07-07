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
        
    def put_new_process(self):
        new_pcb = self.choose_new_process()
        if new_pcb != None:
            self.queue.put(new_pcb)

    def choose_new_process(self):
        # This method chose only the first pcb and put it in the queue
        if self.new_processes:
            return self.new_processes[0]
    