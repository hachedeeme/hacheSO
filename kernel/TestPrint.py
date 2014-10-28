from Print import Print
from Console import Console
import unittest

class TestPrint(unittest.TestCase):
    def test_execute_when_(self):
        console = Console()
        printInst = Print("hache", console)
        printInst.execute()
        self.assertEqual(console.screen, "hache")

if __name__ == '__main__':
    unittest.main()
