import unittest

from src.kernel.Program import Program
from src.kernel.Kernel  import Kernel
from src.instructions.Print import Print

class TestKernel(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel()
        self.program1 = Program('program1')
        self.program1.add_instruction(Print("Hello ", self.kernel.console))
        self.program1.add_instruction(Print("how ", self.kernel.console))
        self.program1.add_instruction(Print("are  ", self.kernel.console))
        self.program1.add_instruction(Print("you?", self.kernel.console))
        #self.kernel.save_program(self.program1)
        
"""    def test_run_when_all_is_fine(self):
        self.kernel.run('program1')
        self.assertEqual(len(self.kernel.long_term_scheduler.new_processes), 1)
        self.assertEqual(self.kernel.pids, 1)"""
        
if __name__ == '__main__':
    unittest.main()