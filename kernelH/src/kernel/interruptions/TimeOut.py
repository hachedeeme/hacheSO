from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Ready

class TimeOut(Interruption):
    
    def manage(self, interruption_manager, pcb):
        pcb.change_state(Ready())
        interruption_manager.get_short_term_scheduler().put_pcb(pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        print("Time Out: Process " + str(pcb.pid) + " state: " + pcb.state.state + " in ready Queue")