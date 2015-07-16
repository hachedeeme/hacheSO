from Interruption import Interruption
from Log import Log
from PcbState import Ready


class TimeOut(Interruption):
    
    def manage(self, interruption_manager):
        self.pcb.change_state(Ready())
        interruption_manager.get_short_term_scheduler().put_pcb(self.pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        Log().print_interruption("Time Out: Process " + str(self.pcb.pid) + " state: " + str(self.pcb.state) + " in ready Queue")