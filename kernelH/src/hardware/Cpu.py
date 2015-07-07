# Cpu
# - current_pcb(Pcb):
#
# + clock_pulse(): Execute one instruction

class Cpu(object):

    def __init__(self, scheduler, mmu):
        self.current_pcb = None
        self.scheduler   = scheduler
        self.mmu         = mmu
        
    def clock_pulse(self):
        self.set_new_pcb()        
        
        if self.have_pcb_to_execute():
            current_inst = self.mmu.fetch_instruction(self.current_pcb.pc)
            
        if not current_inst.is_IO():
            # Print Information
            print("Process ID: " + str(self.current_pcb.pid) + " Instruction: "+ str(current_inst))
                
    def set_new_pcb(self):
        if self.current_pcb == None:
            self.current_pcb = self.get_new_pcb()
    
    def get_new_pcb(self):
        return self.scheduler.choose_new_process()
    
    def have_pcb_to_execute(self):
        return self.current_pcb != None
        
    def remove_pcb(self):
        self.current_pcb = None