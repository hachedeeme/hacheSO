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

from src.kernel.Console import Console
from src.hardware.HardDisk import HardDisk

class Kernel:
    def __init__(self):
        self.pids = 0
        self.console = Console()
        self.hard_disk = HardDisk()

    def save_program(self, program):
        self.hard_disk.save_program(program)
    
    def run(self, programs_name): 
        program = self.hard_disk.get_program(programs_name)
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