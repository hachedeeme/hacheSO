from Console import Console
from Program import Program
from Print import Print
from DeviceManager import DeviceManager
from Memory import Memory

class Kernel:
    def __init__(self):
        self.console = Console()
        self.device_manager = DeviceManager()

    def run(self, programs_name):
    	program = self.device_manager.get_program(programs_name)
    	self.execute_program(program)

    def save_program(self, program):
    	self.device_manager.save_program(program)

    def execute_program(self, program):
    	for inst in program.instructions:
    		inst.execute()

k = Kernel()
pro = Program('p1')
pro.add_instruction(Print("Hola ",k.console))
pro.add_instruction(Print("como ",k.console))
pro.add_instruction(Print("estas",k.console))
pro.add_instruction(Print("?",k.console))

k.save_program(pro)
k.run('p1')

m = Memory()
m.load(pro)

print(m.data)
print(k.console.screen)
