import Queue


class  InterruptionManager:
	def __init__(self):
		self.interruptions = Queue.Queue()

	def handle(self, interruption):
		interruption.execute()