## Instruction
##
## + execute(): execute the instruction.
## + is_IO(): return True if is IO instruction

class Instruction:
    def execute(self):
        raise NotImplementedError("Please Implement this method")

    def is_IO(self):
        return False