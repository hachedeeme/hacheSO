from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Finish

class FinishPcbInIO(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Finish())
        interruption_manager.get_long_term_scheduler().add_finished_processes(self.pcb)
        interruption_manager.get_io_device().remove_pcb()
        interruption_manager.get_mmu().free(self.pcb)
        print(interruption_manager.get_mmu().memory)
        print("IO Finish Process " + str(self.pcb.pid) + " state: " + self.pcb.state.state)