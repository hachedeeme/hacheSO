import unittest

from src.process.Pcb import Pcb

class TestPolicy(unittest.TestCase):
    def setUp(self):
        # Process
        self.pcb = Pcb(0,12,4)
        
    def test_creation(self):
        pass
    
    def test_raise_pc(self):
        self.pcb.raise_pc()
        self.assertEqual(self.pcb.pc, 13)
        self.pcb.raise_pc()
        self.assertEqual(self.pcb.pc, 14)
    
    def test_is_finish(self):
        self.pcb.raise_pc()
        self.assertFalse(self.pcb.is_finish())
        self.pcb.raise_pc()
        self.assertFalse(self.pcb.is_finish())
        self.pcb.raise_pc()
        self.assertFalse(self.pcb.is_finish())
        self.pcb.raise_pc()
        self.assertTrue(self.pcb.is_finish())
    
    def test_change_state(self):
        pass
        
if __name__ == '__main__':
    unittest.main()