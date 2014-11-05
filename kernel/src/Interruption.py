class Interruption:
    def __init__(self):
        raise NotImplementedError("Can't create a Interruption object")

    def execute(self):
    	raise NotImplementedError("Method execute() not define")


class New(Interruption):
	def __init__(self, long_term_scheduler):
		self.cheduler = long_term_scheduler

	def execute(self):
		self

