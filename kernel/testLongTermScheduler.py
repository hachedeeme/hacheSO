from src.Scheduler import LongTermScheduler
import unittest
import Queue


class TestLongTermScheduler:
	def setUp(self):
		self.scheduler = LongTermScheduler(Queue.Queue())

	def test_choose_a_new_process(self):
		self.scheduler.add_new_process(1)
		self.scheduler.choose_new_process()
		

if __name__ == '__main__':
    unittest.main()