from Log import Log
from Interruption import Interruption
from PcbState import Finish


class FinishPcb(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Finish())
        interruption_manager.get_long_term_scheduler().add_finished_processes(self.pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        interruption_manager.get_mmu().free(self.pcb)
        Log().print_memory_state(interruption_manager.get_mmu().memory)
        Log().print_interruption("Finish Process " + str(self.pcb.pid) + " state: " + self.pcb.state.state)