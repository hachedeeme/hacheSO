from src.hardware.Cpu import Cpu
from src.hardware.HardDisk import HardDisk
from src.hardware.Memory import Memory
from src.kernel.Kernel import Kernel
from src.kernel.Log import Log
from src.kernel.Shell import SheelH
from src.memoryManagement.continousAllocation.ContinousAllocation import ContinousAllocation
from src.memoryManagement.continousAllocation.Fits import BestFit
from src.process.Program import Program
from src.process.instructions.Add import Add
from src.process.instructions.Print import Print
from src.scheduling.policies.Fifo import Fifo
from src.memoryManagement.paging.Paging import Paging


memory = Memory(32)
mmu    = ContinousAllocation(memory, BestFit())
mmu    = Paging(memory, 4)
hard_disk = HardDisk()
cpu = Cpu(None, None, None)
scheduling_policy = Fifo()
h_kernel = Kernel(cpu, mmu, hard_disk, scheduling_policy)
h_kernel = Kernel(cpu, mmu, hard_disk)

Log().debug_mode = True

shell = SheelH(h_kernel)
h_kernel.start()

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
pro3.add_instruction(Print("Hola ", h_kernel.console))
pro3.add_instruction(Print("como ", h_kernel.console))
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Add(4,2))
pro3.add_instruction(Print("estas", h_kernel.console))
pro3.add_instruction(Print("?", h_kernel.console))

h_kernel.save_program(pro)
h_kernel.save_program(pro2)
h_kernel.save_program(pro3)


h_kernel.run('program1')
h_kernel.run('program2')
h_kernel.run('program3')

if not Log().debug_mode:
    shell.cmdloop()