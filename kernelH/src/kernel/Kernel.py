import queue

from src.hardware.Clock    import Clock
from src.hardware.Cpu      import Cpu
from src.hardware.HardDisk import HardDisk
from src.hardware.Memory   import Memory
from src.kernel.Console import Console
from src.kernel.InterruptionManager import InterruptionManager
from src.kernel.MemoryManagementUnit    import MemoryManagementUnit
from src.process.Pcb import Pcb
from src.process.Program import Program
from src.process.instructions.Add import Add
from src.process.instructions.Print import Print
from src.scheduling.LongTermScheduler   import LongTermScheduler
from src.scheduling.ShortTermScheduler  import ShortTermScheduler
from src.scheduling.policies.RoundRobin import RoundRobin
from src.kernel.interruptions.NewPcb import NewPcb


class Kernel:
    def __init__(self):
        self.pids    = 0
        self.console = Console()
        
        # Queues
        self.ready_queue = queue.Queue()
        
        # Hardware
        self.memory    = Memory(2048)
        self.hard_disk = HardDisk()
        
        # MMU
        self.mmu = MemoryManagementUnit(self.memory)
        
        # Interruption Manager
        self.interruption_manager = InterruptionManager(self)
        
        # Scheduling
        self.long_term_scheduler  = LongTermScheduler(self.ready_queue)
        self.short_term_scheduler = ShortTermScheduler(self.ready_queue, RoundRobin(3))
    
        # Cpu
        self.cpu = Cpu(self.short_term_scheduler, self.mmu, self.interruption_manager)
        
        self.clock = Clock("Cpu clock", [self.cpu])
        
    #===============  
    #=== Methods === 
    #===============  
    def save_program(self, program):
        self.hard_disk.save_program(program)
    
    def run(self, programs_name):         
        # get program
        program = self.hard_disk.get_program(programs_name)
        
        # create the new pcb with the current id
        new_pcb = self.create_pcb_of(program)
        
        # add the new process to the new process list
        self.long_term_scheduler.add_new_process(new_pcb)
        
        # NewPcb Interruption
        self.interruption_manager.dispatch(NewPcb(), new_pcb)
    
    def create_pcb_of(self, a_program):
        # load the program in memory
        program_counter = self.mmu.load(a_program)
        # create the new Pcb with the current id
        new_pcb = Pcb(self.pids, program_counter, a_program.length())
        self.raise_pid()
        return new_pcb
        
    def raise_pid(self):
        self.pids += 1



k = Kernel()
pro = Program('p1')
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro2 = Program('p2')
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro3 = Program('p3')
pro3.add_instruction(Print("Hola ", k.console))
pro3.add_instruction(Print("como ", k.console))
pro3.add_instruction(Print("estas", k.console))
pro3.add_instruction(Print("?", k.console))

k.save_program(pro)
k.save_program(pro2)
k.save_program(pro3)

k.run('p1')
k.run('p2')

