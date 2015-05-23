## Scheduler
## - ready_queue(Queue(Pcb))..: Queue of the system's Pcbs.
##
## + choose_new_process().....: Choose a Pcb from the ready Queue.

class Scheduler:
	def __init__(self, queue):
		self.ready_queue = queue

	def choose_new_process(self):
		raise NotImplementedError("Please Implement this method")