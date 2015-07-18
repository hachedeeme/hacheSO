import unittest

from src.memoryManagement.continousAllocation.Page import Page
from src.memoryManagement.paging.PageTableUnit import PageTableUnit


class TestPageTableUnit(unittest.TestCase):


    def test_get_physical_direction(self):
        unit = PageTableUnit(4, [Page(0,0,4), Page(0,8,4)])
        
        self.assertEqual(unit.get_physical_direction(0), 0)
        self.assertEqual(unit.get_physical_direction(1), 1)
        self.assertEqual(unit.get_physical_direction(2), 2)
        self.assertEqual(unit.get_physical_direction(3), 3)
        
        self.assertEqual(unit.get_physical_direction(4),  8)
        self.assertEqual(unit.get_physical_direction(5),  9)
        self.assertEqual(unit.get_physical_direction(6), 10)
        self.assertEqual(unit.get_physical_direction(7), 11)

if __name__ == "__main__":
    unittest.main()