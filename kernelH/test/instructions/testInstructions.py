import unittest

from src.hardware.IOdevices.Console   import Console
from src.process.instructions.Add     import Add
from src.process.instructions.Print   import Print
from src.process.instructions.PrintLn import PrintLn

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
        
        # Add instruction isn's IO instruction
        self.assertFalse(Add(1,1).is_IO())
        
        self.assertEqual(str(Add(1,1)), "Add(1,1)")
        
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
        
        # Print instruction is IO instruction
        self.assertTrue(Print('a', self.console).is_IO())
        
        # PrintLn instruction is IO instruction
        self.assertTrue(PrintLn('a', self.console).is_IO())
        
        self.assertEqual(str(Print('a', self.console)), 'Print("a")')
        self.assertEqual(str(PrintLn('a', self.console)), 'PrintLn("a")')
        
        
if __name__ == '__main__':
    unittest.main()