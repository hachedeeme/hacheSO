import unittest

from src.kernel.Console import Console

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()
        
    def test_creation(self):
        # The screen of the console should be empty
        self.assertEqual(self.console.screen, "")
        
    def test_printMessage(self):
        # Print the string 'Hello' in the Console
        self.console.printMessage('Hello')        
        # The screen of the console should be 'Hello'
        self.assertEqual(self.console.screen, 'Hello')
        
        # Print the string ', ' in the Console
        self.console.printMessage(', ')
        # The screen of the console should be 'Hello, '
        self.assertEqual(self.console.screen, 'Hello, ')
        
        # Print the string 'how are you?' in the Console
        self.console.printMessage('how are you?')
        # The screen of the console should be 'Hello, how are you?'
        self.assertEqual(self.console.screen, 'Hello, how are you?')
        
    def test_printLn(self):
        # Print in lane the string 'Hello' in the Console
        self.console.printLn('Hello')        
        # The screen of the console should be 'Hello\n'
        self.assertEqual(self.console.screen, 'Hello\n')
        
        # Print in lane the string 'how are you?' in the Console
        self.console.printLn('how are you?')
        # The screen of the console should be 'Hello\nhow are you?'
        self.assertEqual(self.console.screen, 'Hello\nhow are you?\n')
        
if __name__ == '__main__':
    unittest.main()