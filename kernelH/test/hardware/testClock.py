import time
import unittest

from src.hardware.Clock import Clock

class LisenerCounter():
    def __init__(self):
        self.counter = 0
        
    def make_tick(self):
        self.counter += 1
        print("Make tick, counter = " + str(self.counter))
    

class TestClock(unittest.TestCase):
        
    def test_run_one_clock_for_five_seconds(self):
        lc1 = LisenerCounter()
        lc2 = LisenerCounter()
        lc3 = LisenerCounter()
        clock = Clock("Fist Clock", [lc1,lc2,lc3])
        time.sleep(5)
        clock.stop()
        
    def test_run_two_clocks_for_five_seconds(self):
        lc1 = LisenerCounter()
        lc2 = LisenerCounter()
        lc3 = LisenerCounter()
        clock1 = Clock("Clock1", [lc1,lc2])
        clock2 = Clock("Clock2", [lc2,lc3])
        time.sleep(3)
        clock1.stop()
        time.sleep(2)
        clock2.stop()
       
if __name__ == '__main__':
    unittest.main()