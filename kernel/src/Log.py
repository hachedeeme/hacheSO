
black  = '\033[30m'
red    = '\033[31m'
green  = '\033[32m'
orange = '\033[33m'
blue   = '\033[34m'
purple = '\033[35m'
cyan   = '\033[36m'
yellow = '\033[93m'
pink   = '\033[95m'
lightgrey = '\033[37m'
darkgrey  = '\033[90m'
lightred  = '\033[91m'
lightgreen= '\033[92m'
lightblue = '\033[94m'
lightcyan = '\033[96m'
ENDC      = '\033[0m'

class Log():
    general = ""
    
    memory  = ""
    memory_state_counter = 1
    
    interruptions  = ""
    interruptions_counter = 1
    
    cpu = ""
    cpu_counter = 1
    
    io  = ""
    io_counter = 1
    
    def print_memory_state(self, memory):
        self.general += self.print_ln(memory, blue)
        self.memory  += self.print_ln("Memory State: " + str(self.memory_state_counter))
        self.memory  += self.print_ln(memory)
        self.memory_state_counter += 1
    
    def print_interruption(self, string):
        self.general += self.print_ln(string, orange)
        self.interruptions += self.print_ln("Interruption counter: " + str(self.interruptions_counter))
        self.interruptions += self.print_ln(string)
        self.interruptions_counter += 1
        
    def print_cpu(self, string):
        self.general += self.print_ln(string, green)
        self.cpu += self.print_ln("Cpu instruction executed" + str(self.cpu_counter))
        self.cpu += self.print_ln(string)
        self.cpu_counter += 1
        
    def print_io(self, string):
        self.general += self.print_ln(string, red)
        self.io += self.print_ln("IO instruction executed" + str(self.io_counter))
        self.io += self.print_ln(string)
        self.io_counter += 1
        
    def print_ln(self, obj, color=""):
        end = ""
        if color != "":
            end = ENDC
        return color + str(obj)  + end + '\n'
    
    def print_general(self, obj, color=""):
        self.general += self.print_ln(obj,color)
        
    
    ## Singleton Magic
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Log, cls).__new__(cls, *args, **kwargs)
        return cls._instance
