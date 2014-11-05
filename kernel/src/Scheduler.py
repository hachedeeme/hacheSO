import Queue


class LongTermScheduler:
	def __init__(self, ready_queue):
		self.new_processes = []
		self.ready_queue = ready_queue

	def add_new_process(self, a_pcb):
		self.new_processes.append(a_pcb)

	def choose_new_process(self):
		# This method chose only the firs pcb
		if self.new_processes:
			self.ready_queue.put(self.new_processes[0])


class ShortTermScheduler:
	def __init__(self, ready_queue):
		self.ready_queue = ready_queue