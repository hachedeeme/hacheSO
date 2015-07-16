from Log import Log
from Interruption import Interruption
from PcbState import IOState


class IOInterruption(Interruption):
    
    def __init__(self, pcb, instruction):
        Interruption.__init__(self, pcb)
        self.current_instruction = instruction
        
    def manage(self, interruption_manager):
        self.pcb.change_state(IOState())
        pcb_instr_tuple = (self.pcb, self.current_instruction)
        
        # Add a (pcb,instruction) tuple to IO Device
        interruption_manager.get_io_device().add_pcb_instruction_tuple(pcb_instr_tuple)
        
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        Log().print_interruption("IO Interruption: Process " + str(self.pcb.pid) + " state: " + str(self.pcb.state) + " is in IO Queue")