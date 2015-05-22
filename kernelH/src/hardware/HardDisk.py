## HardDisk
## - programs([Program])...: Dictionary where will save the programs.
##
## + save_program(Program).: Save a Program in disk.
## + get_program(String)...: Returns a Program from the disk by name.

class HardDisk:
    def __init__(self):
        self.programs = {}

    # Save a Program in disk.
    def save_program(self, program):
        self.programs[program.name] = program

    # Returns a Program from the disk by name.
    def get_program(self, programs_name):
        return self.programs[programs_name]
