from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Ready

class TimeOutInIO(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Ready())
        interruption_manager.get_short_term_scheduler().put_pcb(self.pcb)
        interruption_manager.get_io_device().remove_pcb()
        print("Time Out in IO: Process " + str(self.pcb.pid) + " state: " + str(self.pcb.state) + " in ready Queue")