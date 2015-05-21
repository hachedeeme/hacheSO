
class HardDisk:
    def __init__(self):
        self.programs = {}

    # Save a Program in disk
    def save_program(self, program):
        self.programs[program.name] = program

    # Returns a Program from the disk
    def get_program(self, programs_name):
        return self.programs[programs_name]
