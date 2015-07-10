from src.hardware.Clock import Clock
from src.process.PcbState import IOState


class IODevice():
    def __init__(self, interruption_manager):
        self.io_queue    = []
        self.current_pcb = None
        self.interruption_manager = interruption_manager
        self.clock = Clock("IO Clock", [self])
        
        def clock_pulse(self):
            self.set_new_pcb()
            
            if self.have_pcb_to_execute():
                self.current_pcb.change_state(IOState())
                # Print Information
                print("IO Execution - Process ID: " + str(self.current_pcb.pid) + " Instruction: " + str() + " State: " + str(self.current_pcb.state))
                #current_inst.execute()
                self.current_pcb.raise_pc()
            
        def set_new_pcb(self):
            if self.io_queue and not self.current_pcb:
                self.current_pcb = self.io_queue.pop(0)
                
        def have_pcb_to_execute(self):
            return self.current_pcb
        
        def remove_pcb(self):
            self.current_pcb = None

        def start(self):
            self.clock.start()