import unittest

from src.process.Pcb import Pcb

class TestPolicy(unittest.TestCase):
    def setUp(self):
        # Process
        self.pcb = Pcb(0,12,12)
        
    def test_creation(self):
        pass
    
    def test_change_state(self):
        pass
        
if __name__ == '__main__':
    unittest.main()