import threading
import time

from Log import Log


class Clock(threading.Thread):
    def __init__(self, name, listeners):
        super().__init__()
        self.name = name
        self.tick = 0
        self.running   = True
        self.listeners = listeners
        
    def run(self):
        while self.running:
            self.tick += 1
            Log().print_general(self.name + " tick " + str(self.tick))
            
            for lisener in self.listeners:
                lisener.clock_pulse()
            
            # Sleep one second
            time.sleep(1)
    
    def reset(self):
        self.running = True
        self.start()
        
    def stop(self):
        self.running = False
        Log().print_general(self.name + " stop")