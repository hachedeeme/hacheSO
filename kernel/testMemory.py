from src.Memory import Memory
from src.Program import Program
from src.Add import Add
import unittest


class TestPrint(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_load_a_program(self):
        self.assertEqual(self.memory.current_dir, 0)
        p1 = Program('p1')
        p1.add_instruction(Add(1, 1))
        p1.add_instruction(Add(1, 1))
        p1.add_instruction(Add(1, 1))
        first_dir = self.memory.load(p1)
        self.assertEqual(self.memory.current_dir, 3)
        self.assertEqual(first_dir, 0)
        self.assertEqual(len(self.memory.data), 3)

        p2 = Program('p2')
        p2.add_instruction(Add(1, 1))
        first_dir = self.memory.load(p2)
        self.assertEqual(self.memory.current_dir, 4)
        self.assertEqual(first_dir, 3)
        self.assertEqual(len(self.memory.data), 4)

if __name__ == '__main__':
    unittest.main()