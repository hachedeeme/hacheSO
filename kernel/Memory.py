class Memory:
    def __init__(self):
        self.data = {}
        self.length = 0
        self.current_dir = 0

    def read(self, dir_mem):
        return self.data[dir_mem]

    def write(self, dir_mem, instruction):
        self.data[dir_mem] = instruction

    def load(self, program):
        for instruction in program.instructions:
            self.write(self.current_dir, instruction)
            self.current_dir += 1
