from Add import Add
from ContinousAllocation import ContinousAllocation
from Cpu import Cpu
from Fifo import Fifo
from Fits import BestFit
from HardDisk import HardDisk
from Kernel import Kernel
from Memory import Memory
from Print import Print
from Program import Program
from Shell import SheelH

memory = Memory(32)
mmu    = ContinousAllocation(memory, BestFit())
hard_disk = HardDisk()
cpu = Cpu(None, None, None)
scheduling_policy = Fifo()
k = Kernel(cpu, mmu, hard_disk)
k = Kernel(cpu, mmu, hard_disk, scheduling_policy)

shell = SheelH(k)
k.start()

pro = Program('program1')
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro.add_instruction(Add(1,2))
pro2 = Program('program2')
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro2.add_instruction(Add(3,2))
pro3 = Program('program3')
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Print("Hola ", k.console))
pro3.add_instruction(Print("como ", k.console))
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Print("estas", k.console))
pro3.add_instruction(Print("?", k.console))

k.save_program(pro)
k.save_program(pro2)
k.save_program(pro3)

shell.cmdloop()