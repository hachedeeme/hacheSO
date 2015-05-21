import unittest

from src.hardware.HardDisk import HardDisk
from src.kernel.Program import Program

class TestHardDisk(unittest.TestCase):
    def setUp(self):
        # Hard Disk Drive
        self.disk = HardDisk()
        
        # Programs
        self.program1 = Program('Program 1')
        self.program2 = Program('Program 2')
        
    def test_empty_hard_disk(self):
        # The HardDisk data is empty.
        self.assertEqual(len(self.disk.programs), 0)

    def test_save_and_get_a_program(self):
        # Save the program1 on the HardDisk
        self.disk.save_program(self.program1)
        
        # When get the 'Program 1' from Disk, it should be the program1
        self.assertEqual(self.disk.get_program('Program 1'), self.program1)
        
        # Save the program2 on the HardDisk
        self.disk.save_program(self.program2)
        
        # When get the 'Program 2' from Disk, it should be the program2
        self.assertEqual(self.disk.get_program('Program 2'), self.program2)
       
if __name__ == '__main__':
    unittest.main()