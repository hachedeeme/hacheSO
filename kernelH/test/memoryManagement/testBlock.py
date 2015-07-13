import unittest

from src.memoryManagement.continousAllocation.Block import Block


class TestBlock(unittest.TestCase):
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
        
    def test_subtract(self):
        new_free_block = self.block.subtract(Block(0,5))
        self.assertEqual(new_free_block.base, 5)
        self.assertEqual(new_free_block.limit, 3)
        
        new_free_block = self.block.subtract(Block(0,8))
        self.assertEqual(new_free_block, None)