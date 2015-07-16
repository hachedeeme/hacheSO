## Memory
## - data(Dictionary)......: Dictionary representing the data of memory.
## - size(Integer).........: Size of the memory.
## - current_dir(Integer)..: Memory direction where will start save a program.
##
## + read(Integer)..............: Read the direction dir_mem of the memory and 
##                                returns the instruction located on it.
## + write(Integer, Instruction): Write an instruction in the direction dir_mem of the memory.
## + load(Program)..............: Load a program in memory and return the first direction
##                                where the program start. 
## + usedSpace()................: Returns the space use of the memory.
## + get_free_blocks()..........: Get the free blocks list of the memory.
## + free(Integer,Integer)......: Free a block of memory, fist parameter base_dir, second parameter limit.
## + free_direction(Integer)....: Free the direction parameter.

from src.memoryManagement.continousAllocation.Block import Block

class Memory:
    def __init__(self, memory_size):
        self.data = {}
        self.size = memory_size
        self.current_dir = 0
        for index_dir in range(0, self.size):
            self.data[index_dir] = {"used":False, "data":None}

    def read(self, dir_mem):
        return self.data[dir_mem]["data"]

    def write(self, dir_mem, instruction):
        self.data[dir_mem]["data"] = instruction
        self.data[dir_mem]["used"] = True

    def load(self, program):
        first_dir = self.current_dir
        for instruction in program.instructions:
            self.write(self.current_dir, instruction)
            self.current_dir += 1
        return first_dir
    
    def load_program_to_block(self, program, free_block):
        self.current_dir = free_block.base
        for instruction in program.instructions:
            self.write(self.current_dir, instruction)
            self.current_dir += 1
        return Block(free_block.base, program.length())
    
    def get_first_free_dir(self):
        current = 0
        for index_dir in range(0, self.size):
            if self.data[index_dir]["used"]:
                current += 1
            else:
                break
        return current
    
    def move(self, a_block, mem_dir):
        last_base_dir = a_block.base
        a_block.set_base(mem_dir)
        for _ in range(a_block.limit):
            instruction = self.read(last_base_dir)
            self.free_direction(last_base_dir)
            self.write(mem_dir, instruction)
            last_base_dir += 1
            mem_dir += 1
        return a_block

    def used_space(self):
        count = 0
        for index_dir in range(0, self.size):
            if self.data[index_dir]["used"]:
                count += 1
        return count
    
    def free(self, base_dir, limit):
        for current_dir in range(base_dir, base_dir + limit):
            self.free_direction(current_dir)
    
    def free_direction(self, dir_mem):
        self.data[dir_mem] = {"used":False, "data":None}
    
    def is_use_direction(self, dir_mem):
        return self.data[dir_mem]["used"]
        
    def __str__(self):
        str_mem = ""
        for index_dir in range(0, self.size):
            if index_dir < 10:
                str_mem += '000'
            elif index_dir < 100:
                str_mem += '00'
            elif index_dir < 1000:
                str_mem += '0'
            str_mem += str(index_dir) + ' { '
            str_mem += 'used: ' + str(self.data[index_dir]["used"]) + ' '
            str_mem += 'data: ' + str(self.data[index_dir]["data"]) + ' }\n'
        return str_mem

