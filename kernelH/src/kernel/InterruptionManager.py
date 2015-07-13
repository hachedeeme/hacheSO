
class InterruptionManager():
    def __init__(self, kernel):
        self.kernel = kernel
        self.interruptions = []
    
    def dispatch(self, interruption):
        self.interruptions.append(interruption)
    
    def manage(self, interruption):
        interruption.manage(self)
        
    def clock_pulse(self):
        while self.interruptions:
            current_interruption = self.interruptions.pop(0)
            self.manage(current_interruption)
    
    #===============#
    #=== Getters ===#    
    #===============#
    def get_long_term_scheduler(self):
        return self.kernel.long_term_scheduler
    
    def get_short_term_scheduler(self):
        return self.kernel.short_term_scheduler
    
    def get_cpu(self):
        return self.kernel.cpu
    
    def get_io_device(self):
        return self.kernel.io
    
    def get_mmu(self):
        return self.kernel.mmu