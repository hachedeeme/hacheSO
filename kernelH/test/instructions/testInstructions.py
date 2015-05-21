import unittest

from src.kernel.Console import Console
from src.instructions.Add     import Add
from src.instructions.Print   import Print
from src.instructions.PrintLn import PrintLn

class TestInstructions(unittest.TestCase):
    def setUp(self):
        self.console = Console()
        
    def test_Add(self):
        # Execute an Add instruction with 2 and 2 should be 4
        self.assertEqual(Add(2,2).execute(), 4)
        
        # Execute an Add instruction with 0 and 0 should be 0
        self.assertEqual(Add(0,0).execute(), 0)
        
        # Execute an Add instruction with -2 and -2 should be -4
        self.assertEqual(Add(-2,-2).execute(), -4)
        
    def test_Print_and_PrintLn(self):
        # Execute a Print instruction with the message 'Hello' should 
        # print 'Hello' in the console screen.
        Print('Hello', self.console).execute()
        self.assertEqual(self.console.screen, 'Hello')
        
        # Execute a Print instruction with the message ', ' should 
        # print 'Hello, ' in the console screen.
        Print(', ', self.console).execute()
        self.assertEqual(self.console.screen, 'Hello, ')
        
        # Execute a Print instruction with the message 'how are you?' should 
        # print 'Hello, how are you?\n' in the console screen.
        PrintLn('how are you?', self.console).execute()
        self.assertEqual(self.console.screen, 'Hello, how are you?\n')
        
if __name__ == '__main__':
    unittest.main()