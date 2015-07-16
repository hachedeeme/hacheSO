
class OutOfMemory(Exception):
    def __str__(self):
        return "Not enough memory for this process"