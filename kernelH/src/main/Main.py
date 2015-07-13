from src.hardware.Cpu import Cpu
from src.hardware.HardDisk import HardDisk
from src.hardware.Memory import Memory
from src.kernel.Kernel import Kernel
from src.memoryManagement.continousAllocation.ContinousAllocation import ContinousAllocation
from src.memoryManagement.continousAllocation.Fits import BestFit
from src.process.Program import Program
from src.process.instructions.Add import Add
from src.process.instructions.Print import Print
from src.scheduling.policies.Fifo import Fifo


memory = Memory(32)
mmu    = ContinousAllocation(memory, BestFit())
hard_disk = HardDisk()
cpu = Cpu(None, None, None)
scheduling_policy = Fifo()

k = Kernel(cpu, mmu, hard_disk, scheduling_policy)
k = Kernel(cpu, mmu, hard_disk)
k.start()

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

k.run('p1')
k.run('p2')
k.run('p3')
