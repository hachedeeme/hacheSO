from src.kernel.interruptions.Interruption import Interruption


class FinishPcb(Interruption):
    
    def manage(self, interruption_manager, pcb):
        pcb.change_state('FINISH')
        interruption_manager.get_long_term_scheduler().add_finished_processes(pcb)
        interruption_manager.get_short_term_scheduler().reset_quantum()
        interruption_manager.get_cpu().remove_pcb()
        print("Process " + str(pcb.pid) + " state: " + pcb.state)
        print(str(interruption_manager.get_cpu().current_pcb))
        