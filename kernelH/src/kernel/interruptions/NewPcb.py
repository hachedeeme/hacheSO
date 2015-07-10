from src.kernel.interruptions.Interruption import Interruption

class NewPcb(Interruption):
    def __init__(self):
        pass
    
    def manage(self, interruption_manager):
        interruption_manager.get_long_term_scheduler().put_new_process_in_ready()