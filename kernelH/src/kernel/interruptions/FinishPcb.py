from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Finish


class FinishPcb(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Finish())
        interruption_manager.get_long_term_scheduler().add_finished_processes(self.pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        print("Process " + str(self.pcb.pid) + " state: " + self.pcb.state.state)