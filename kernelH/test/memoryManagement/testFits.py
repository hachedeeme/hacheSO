import unittest

from src.kernel.memoryManagement.continousAllocation.Block import Block

class TestFits(unittest.TestCase):
    def setUp(self):
        self.block = Block(0,8)
    
    def test_creation(self):
        self.assertEqual(self.block.base, 0)
        self.assertEqual(self.block.limit, 8)
        self.assertTrue(self.block.is_free())
        
    def test_last_dir(self):
        self.assertEqual(self.block.last_dir(), 7)
        self.assertEqual(Block(100, 20).last_dir(), 119)
        
    def test_belongs(self):
        for i in range(0,7):
            self.assertTrue(self.block.belongs(i))
            
        self.assertFalse(self.block.belongs(8))
        self.assertFalse(self.block.belongs(100))
        self.assertFalse(self.block.belongs(1000))