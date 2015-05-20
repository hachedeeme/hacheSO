
class Memory:
    def __init__(self):
        self.data = {}
        self.size = 0
        self.current_dir = 0

    # Read the direction dir_mem of the memory and returns the
    # instruction located on it.
    def read(self, dir_mem):
        return self.data[dir_mem]

    # Write an instruction in the direction dir_mem of the memory. 
    def write(self, dir_mem, instruction):
        self.data[dir_mem] = instruction

    # Load a program in memory and return the first direction
    # where the program start. 
    def load(self, program):
        first_dir = self.current_dir
        for instruction in program.instructions:
            self.write(self.current_dir, instruction)
            self.current_dir += 1
        return first_dir
    
    # Returns the space use of the memory.
    def usedSpace(self):
        return len(self.data)