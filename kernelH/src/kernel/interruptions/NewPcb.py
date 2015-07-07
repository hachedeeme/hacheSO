from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Ready

class NewPcb(Interruption):
    
    def manage(self, interruption_manager, pcb):
        pcb.change_state(Ready())
        interruption_manager.get_long_term_scheduler().put_new_process()