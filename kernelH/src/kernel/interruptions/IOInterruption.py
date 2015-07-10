from src.kernel.interruptions.Interruption import Interruption
from src.process.instructions.IOInstruction import IOInstruction

class IOInterruption(Interruption):
    
    def manage(self, interruption_manager, pcb):
        self.pcb.change_state(IOInstruction())
        interruption_manager.get_short_term_scheduler().put_pcb(self.pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        print("Time Out: Process " + str(self.pcb.pid) + " state: " + self.pcb.state.state + " in ready Queue")