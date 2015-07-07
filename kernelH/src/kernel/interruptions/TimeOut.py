from src.kernel.interruptions.Interruption import Interruption

class TimeOut(Interruption):
    
    def manage(self, interruption_manager, pcb):
        raise NotImplementedError("Please Implement this method")