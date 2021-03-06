from src.kernel.Log import Log
from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Finish


class FinishPcbInIO(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Finish())
        interruption_manager.get_long_term_scheduler().add_finished_processes(self.pcb)
        interruption_manager.get_mmu().free(self.pcb)
        Log().print_memory_state(interruption_manager.get_mmu().memory)
        Log().print_interruption("IO Finish Process " + str(self.pcb.pid) + " state: " + self.pcb.state.state)