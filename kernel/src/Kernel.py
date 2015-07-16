import queue

from Pcb                    import Pcb
from Clock                 import Clock
from Console     import Console
from IODevice    import IODevice
from InterruptionManager     import InterruptionManager
from NewPcb    import NewPcb
from LongTermScheduler   import LongTermScheduler
from ShortTermScheduler  import ShortTermScheduler
from RoundRobin import RoundRobin

class Kernel:
    def __init__(self, cpu, mmu, hard_disk, scheduling_policy=RoundRobin(3)):
        self.pids    = 0
        # Queues
        self.ready_queue = queue.Queue()
        
        # Hardware
        self.hard_disk = hard_disk
        self.mmu       = mmu
        
        # Interruption Manager
        self.interruption_manager = InterruptionManager(self)
        
        # Scheduling
        self.short_term_scheduler = ShortTermScheduler(self.ready_queue, scheduling_policy)
        self.long_term_scheduler  = LongTermScheduler(self.ready_queue)
    
        # Cpu
        self.cpu = cpu
        self.cpu.set_scheduler(self.short_term_scheduler)
        self.cpu.set_mmu(self.mmu)
        self.cpu.set_interruption_manager(self.interruption_manager)
        
        # IO
        self.console = Console()
        self.io = IODevice(self.interruption_manager)
        
        self.clock = Clock("Cpu - IntManager clock", [self.cpu, self.interruption_manager])
        
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
        self.interruption_manager.dispatch(NewPcb())
    
    def create_pcb_of(self, a_program):
        # load the program in memory
        program_counter = self.mmu.load(a_program)
        
        # create the new Pcb with the current id
        new_pcb = Pcb(self.pids, program_counter, a_program.length())
        self.raise_pid()
        
        return new_pcb
        
    def raise_pid(self):
        self.pids += 1
    
    def start(self):
        self.clock.start()
        self.io.start()
        
    def stop(self):
        self.clock.stop()
        self.io.clock.stop()
        