from Clock import Clock
from Log import Log
from FinishPcbInIO import FinishPcbInIO
from TimeOutInIO import TimeOutInIO
from PcbState import IOState

class IODevice():
    def __init__(self, interruption_manager):
        self.io_queue    = []
        self.current_pcb_tuple = None
        self.interruption_manager = interruption_manager
        self.clock = Clock("IO Clock", [self])
        
    def add_pcb_instruction_tuple(self, pcb_tuble):
        self.io_queue.append(pcb_tuble)
    
    def clock_pulse(self):
        self.set_new_pcb()
        
        if self.have_pcb_to_execute():
            current_pcb = self.get_pcb()
            current_inst = self.get_instruction()
            
            # Change pcb state to IOState
            current_pcb.change_state(IOState())
            
            # Execute instruction
            current_inst.execute()
            
            # Print Information
            # print("IO Execution - Process ID: " + str(current_pcb.pid) + " Instruction: " + str(current_inst) + " State: " + str(current_pcb.state))
            Log().print_io("IO Execution - Process ID: " + str(current_pcb.pid) + " Instruction: " + str(current_inst) + " State: " + str(current_pcb.state))
            
            # Raise pc
            current_pcb.raise_pc()
            
            if current_pcb.is_finish():
                # Make Finish interruption
                self.interruption_manager.dispatch(FinishPcbInIO(current_pcb))
                self.remove_pcb()
            else:
                # Make TimeOut interruption
                self.interruption_manager.dispatch(TimeOutInIO(current_pcb))
                self.remove_pcb()
        
    def set_new_pcb(self):
        if self.io_queue and not self.current_pcb_tuple:
            self.current_pcb_tuple = self.io_queue.pop(0)
            
    def have_pcb_to_execute(self):
        return self.current_pcb_tuple
    
    def remove_pcb(self):
        self.current_pcb_tuple = None

    def start(self):
        self.clock.start()
        
    def get_pcb(self):
        return self.current_pcb_tuple[0]
        
    def get_instruction(self):
        return self.current_pcb_tuple[1]