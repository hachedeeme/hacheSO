## LongTermScheduler
## - ready_queue(Queue(Pcb))..: Queue of the system's Pcbs.
## - new_processes([Pcb]).....: List of the news processes.
##
## + add_new_process(Pcb).........: Add a new Pcb to the list of processes.
## + choose_new_process().........: Choose the first pcb of the new processes list if there is.
## + add_finished_processes(Pcb)..: Put the pcb in the finished processes list.

from PcbState     import Ready
from Scheduler import Scheduler


class LongTermScheduler(Scheduler):
    def __init__(self, queue):
        super().__init__(queue)
        self.new_processes      = []
        self.finished_processes = []

    def choose_new_process(self):
        # This method chose only the first pcb of the new processes list if there is.
        if self.new_processes:
            return self.new_processes.pop(0)
        
    def put_new_process_in_ready(self):
        new_pcb = self.choose_new_process()
        if new_pcb != None:
            new_pcb.change_state(Ready())
            self.queue.put(new_pcb)

    def add_new_process(self, a_pcb):
        self.new_processes.append(a_pcb)
        
    def add_finished_processes(self, a_pcb):
        self.finished_processes.append(a_pcb)
        