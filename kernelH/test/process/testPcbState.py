import unittest

from src.process.PcbState import *

class TestPcbState(unittest.TestCase):
        
    def test_str(self):
        self.assertEqual(str(New()),     'NEW')
        self.assertEqual(str(Ready()),   'READY')
        self.assertEqual(str(Running()), 'RUNNING')
        self.assertEqual(str(Finish()),  'FINISH')
        self.assertEqual(str(IOState()), 'IO')
    
if __name__ == '__main__':
    unittest.main()