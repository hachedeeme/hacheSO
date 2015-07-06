# Cpu
# - current_pcb(Pcb):
#
# + clock_pulse(): Execute one instruction

class Cpu(object):

    def __init__(self, kernel):
        self.kernel = kernel
        self.short_term_scheduller = kernel.short_term_scheduller
        self.current_pcb = None
        
        
    def clock_pulse(self):
        pass