import time
import threading

class Clock(threading.Thread):
    def __init__(self, name, listeners):
        super().__init__()
        self.name = name
        self.tick = 0
        self.running   = True
        self.listeners = listeners
        # start clock
        self.start()
        
    def run(self):
        while self.running:
            self.tick += 1
            print(self.name + " tick " + str(self.tick))
            
            for lisener in self.listeners:
                lisener.clock_pulse()
            
            # Sleep one second
            time.sleep(1)
    
    def reset(self):
        self.running = True
        self.start()
        
    def stop(self):
        self.running = False
        print(self.name + " stop")