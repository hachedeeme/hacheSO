from src.Print import Print
from src.Console import Console
import unittest


class TestPrint(unittest.TestCase):
    def test_execute_when_print_hache(self):
        console = Console()
        printInst = Print("hache", console)
        printInst.execute()
        self.assertEqual(console.screen, "hache")

if __name__ == '__main__':
    unittest.main()
