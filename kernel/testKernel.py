from src.Print import Print
from src.Program import Program
from src.Kernel import Kernel
import unittest

#test re loco de la cosa loca que va a testear cosas re locas
#test re loco de la cosa loca que va a testear cosas re locas
#test re loco de la cosa loca que va a testear cosas re locas


class TestKernel(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel()
        self.pro1 = Program('pro1')
        self.pro1.add_instruction(Print("Hola ", self.kernel.console))
        self.pro1.add_instruction(Print("como  ", self.kernel.console))
        self.pro1.add_instruction(Print("estas? ", self.kernel.console))
        self.kernel.save_program(self.pro1)

    def test_run_when_all_is_fine(self):
        self.kernel.run('pro1')
        self.assertEqual(len(self.kernel.processes), 1)


if __name__ == '__main__':
    unittest.main()