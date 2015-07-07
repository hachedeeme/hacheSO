from src.kernel.interruptions.Interruption import Interruption

class NewPcb(Interruption):
    
    def manage(self, interruption_manager, pcb):
        raise NotImplementedError("Please Implement this method")