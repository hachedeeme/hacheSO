"""from Console import Console
from Program import Program
from Print import Print
from DeviceManager import DeviceManager
from Memory import Memory
from Pcb import Pcb
from InterruptionManager import InterruptionManager
from Interruption import *
from Scheduler import *
import Queue"""

import queue

from src.hardware.HardDisk import HardDisk
from src.hardware.Memory   import Memory
from src.hardware.Cpu      import Cpu

from src.kernel.Console import Console

from src.scheduling.LongTermScheduler   import LongTermScheduler
from src.scheduling.ShortTermScheduler  import ShortTermScheduler
from src.scheduling.policies.RoundRobin import RoundRobin
from src.kernel.MemoryManagementUnit    import MemoryManagementUnit

from src.process.Pcb import Pcb


class Kernel:
    def __init__(self):
        self.pids    = 0
        self.console = Console()
        
        # Queues
        self.ready_queue = queue.Queue()
        self.news_queue  = queue.Queue()
        
        # Hardware
        self.memory    = Memory(2048)
        self.hard_disk = HardDisk()
        # MMU
        self.mmu = MemoryManagementUnit(self.memory)
        
        # Scheduling
        self.long_term_scheduler  = LongTermScheduler(self.ready_queue)
        self.short_term_scheduler = ShortTermScheduler(self.ready_queue, RoundRobin(3))
    
        # Cpu
        self.cpu = Cpu(self.short_term_scheduler, self.mmu)
        
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
    
    def create_pcb_of(self, a_program):
        # load the program in memory
        program_counter = self.mmu.load(a_program)
        # create the new Pcb with the current id
        new_pcb = Pcb(self.pids, program_counter, a_program.length())
        self.raise_pid()
        return new_pcb
        
    def raise_pid(self):
        self.pids += 1
        
"""    def run(self, programs_name):
        program = self.device_manager.get_program(programs_name)
        first_dir = self.device_manager.load_program(program)
        self.execute_program(program)
        self.long_term_scheduler.add_new_process(Pcb(self.pids, first_dir, program.length()))
        self.pids += 1
        self.interruption_manager.handle(New(self.long_term_scheduler))"""
"""        self.ready_queue = Queue.Queue()

        # devices
        self.device_manager       = DeviceManager()
        self.interruption_manager = InterruptionManager()
        # schedulers
        self.long_term_scheduler  = LongTermScheduler(self.ready_queue)
        self.short_term_scheduler = ShortTermScheduler(self.ready_queue)
"""
       

"""    def execute_program(self, program):
        for inst in program.instructions:
            inst.execute()

k = Kernel()
pro = Program('p1')
pro.add_instruction(Print("Hola ", k.console))
pro.add_instruction(Print("como ", k.console))
pro.add_instruction(Print("estas", k.console))
pro.add_instruction(Print("?", k.console))

k.save_program(pro)
k.run('p1')

m = Memory()
m.load(pro)

print((k.console.screen))"""