import unittest

from src.hardware.Memory import Memory
from src.memoryManagement.continousAllocation.Block import Block
from src.memoryManagement.continousAllocation.Fits  import FirstFit, BestFit, WorstFit
from src.process.Program import Program
from src.process.instructions.Add import Add


class TestFits(unittest.TestCase):
    def setUp(self):
        # Memory
        self.memory = Memory(1024)
        
        # Programs
        self.program1 = Program('p1')
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        self.program1.add_instruction(Add(1, 1))
        
        self.program2 = Program('p2')
        self.program2.add_instruction(Add(1, 1))
        self.program2.add_instruction(Add(1, 1))
        
        self.program3 = Program('p3')
        self.program3.add_instruction(Add(1, 1))
        self.program3.add_instruction(Add(1, 1))
        self.program3.add_instruction(Add(1, 1))
        
        self.program4 = Program('p4')
        self.program4.add_instruction(Add(1, 1))
        self.program4.add_instruction(Add(1, 1))
        self.program4.add_instruction(Add(1, 1))
        self.program4.add_instruction(Add(1, 1))
        
        program1_base = self.memory.load(self.program1)
        self.memory.load(self.program2)
        program3_base = self.memory.load(self.program3)
        self.memory.load(self.program4)
        
        # Free the program 1.
        self.memory.free(program1_base, self.program1.length())
        
        # Free the program 3.
        self.memory.free(program3_base, self.program3.length())
        
        #===== Fits =====#
        # First Fit        
        self.fist = FirstFit()
        self.fist.init_free_blocks_of(self.memory)
        
        # Best Fit        
        self.best = BestFit()
        self.best.init_free_blocks_of(self.memory)
        
        # Best Fit        
        self.worst = WorstFit()
        self.worst.init_free_blocks_of(self.memory)
    
    ###===================###
    ### Test for Fist Fit ###    
    ###===================###   
    def test_first_fit_creation_with_init_free_blocks_of(self):
        self.assertEqual(len(self.fist.free_blocks), 3)
        
        self.assertEqual(self.fist.free_blocks[0].base, 0)
        self.assertEqual(self.fist.free_blocks[0].limit, 8)
        
        self.assertEqual(self.fist.free_blocks[1].base, 10)
        self.assertEqual(self.fist.free_blocks[1].limit, 3)
        
        self.assertEqual(self.fist.free_blocks[2].base, 17)
        self.assertEqual(self.fist.free_blocks[2].limit, 1007)
        
    def test_first_fit_choose_free_block_with_limit_3(self):
        choosen = self.fist.free_blocks[0]
        self.assertEqual(self.fist.choose_free_block(3), choosen)
        
    def test_first_fit_choose_free_block_with_limit_8(self):
        choosen = self.fist.free_blocks[0]
        self.assertEqual(self.fist.choose_free_block(8), choosen)
        
    def test_first_fit_choose_free_block_with_limit_10(self):
        choosen = self.fist.free_blocks[2]
        self.assertEqual(self.fist.choose_free_block(10), choosen)
    
    ###===================###
    ### Test for Best Fit ###    
    ###===================###   
    def test_best_fit_creation_with_init_free_blocks_of(self):
        self.assertEqual(len(self.best.free_blocks), 3)
        
        self.assertEqual(self.best.free_blocks[0].base, 10)
        self.assertEqual(self.best.free_blocks[0].limit, 3)
        
        self.assertEqual(self.best.free_blocks[1].base, 0)
        self.assertEqual(self.best.free_blocks[1].limit, 8)
        
        
        self.assertEqual(self.best.free_blocks[2].base, 17)
        self.assertEqual(self.best.free_blocks[2].limit, 1007)
        
    def test_best_fit_order_when_add_block(self):
        new_block = Block(20, 12)
        # add the new block
        self.best.add_free_block(new_block)
        
        # then the free blocks list length should be 4.
        self.assertEqual(len(self.best.free_blocks), 4)
        
        # and new block should be in the index 2.
        self.assertEqual(self.best.free_blocks[2], new_block)
        
        new_block = Block(500, 1)
        # add the new block
        self.best.add_free_block(new_block)
        
        # then the free blocks list length should be 5.
        self.assertEqual(len(self.best.free_blocks), 5)
        
        # and new block should be in the index 0.
        self.assertEqual(self.best.free_blocks[0], new_block)
        
        new_block = Block(600, 1)
        # add the new block
        self.best.add_free_block(new_block)
        
        # then the free blocks list length should be 6.
        self.assertEqual(len(self.best.free_blocks), 6)
        
        # and new block should be in the index 0.
        self.assertEqual(self.best.free_blocks[0], new_block)
        
        new_block = Block(41, 3)
        # add the new block
        self.best.add_free_block(new_block)
        
        # then the free blocks list length should be 7.
        self.assertEqual(len(self.best.free_blocks), 7)
        
        # and new block should be in the index 0.
        self.assertEqual(self.best.free_blocks[2], new_block)
        
        
    def test_best_fit_choose_free_block_with_limit_3(self):
        choosen = self.best.free_blocks[0]
        self.assertEqual(self.best.choose_free_block(3), choosen)
        
    def test_best_fit_choose_free_block_with_limit_8(self):
        choosen = self.best.free_blocks[1]
        self.assertEqual(self.best.choose_free_block(8), choosen)
        
    def test_best_fit_choose_free_block_with_limit_10(self):
        choosen = self.best.free_blocks[2]
        self.assertEqual(self.best.choose_free_block(10), choosen)
    
    ###===================###
    ### Test for Worst Fit ###    
    ###===================###   
    def test_worst_fit_creation_with_init_free_blocks_of(self):
        self.assertEqual(len(self.worst.free_blocks), 3)
        
        self.assertEqual(self.worst.free_blocks[0].base, 17)
        self.assertEqual(self.worst.free_blocks[0].limit, 1007)
        
        self.assertEqual(self.worst.free_blocks[1].base, 0)
        self.assertEqual(self.worst.free_blocks[1].limit, 8)
        
        self.assertEqual(self.worst.free_blocks[2].base, 10)
        self.assertEqual(self.worst.free_blocks[2].limit, 3)
        
        
    def test_worst_fit_choose_free_block_with_limit_3(self):
        choosen = self.worst.free_blocks[0]
        self.assertEqual(self.worst.choose_free_block(3), choosen)
        
    def test_worst_fit_choose_free_block_with_limit_8(self):
        choosen = self.worst.free_blocks[0]
        self.assertEqual(self.worst.choose_free_block(8), choosen)
        
    def test_worst_fit_choose_free_block_with_limit_10(self):
        choosen = self.worst.free_blocks[0]
        self.assertEqual(self.worst.choose_free_block(10), choosen)
        
    def test_worst_fit_order_when_add_block(self):
        new_block = Block(20, 12)
        # add the new block
        self.worst.add_free_block(new_block)
        
        # then the free blocks list length should be 4.
        self.assertEqual(len(self.worst.free_blocks), 4)
        
        # and new block should be in the index 1.
        self.assertEqual(self.worst.free_blocks[1], new_block)
        
        new_block = Block(20, 1200)
        # add the new block
        self.worst.add_free_block(new_block)
        
        # then the free blocks list length should be 5.
        self.assertEqual(len(self.worst.free_blocks), 5)
        
        # and new block should be in the index 0.
        self.assertEqual(self.worst.free_blocks[0], new_block)

        new_block = Block(20, 1)
        # add the new block
        self.worst.add_free_block(new_block)
        
        # then the free blocks list length should be 6.
        self.assertEqual(len(self.worst.free_blocks), 6)
        
        # and new block should be in the index 5.
        self.assertEqual(self.worst.free_blocks[5], new_block)

        
if __name__ == '__main__':
    unittest.main()