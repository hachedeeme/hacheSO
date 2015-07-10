
class Interruption():
    
    def __init__(self, pcb):
        self.pcb = pcb
    
    def manage(self, interruption_manager):
        raise NotImplementedError("Please Implement this method")