
class InterruptionManager():
    def __init__(self, kernel):
        self.kernel = kernel
    
    def dispatch(self, interruption):
        interruption.manage(self)
    
    #===============#
    #=== Getters ===#    
    #===============#
    def get_long_term_scheduler(self):
        return self.kernel.long_term_scheduler
    
    def get_short_term_scheduler(self):
        return self.kernel.short_term_scheduler
    
    def get_cpu(self):
        return self.kernel.cpu