from src.kernel.Log import Log
from src.kernel.interruptions.Interruption import Interruption
from src.process.PcbState import Ready


class TimeOutInIO(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Ready())
        interruption_manager.get_short_term_scheduler().put_pcb(self.pcb)
        Log().print_interruption("Time Out in IO: Process " + str(self.pcb.pid) + " state: " + str(self.pcb.state) + " in ready Queue")