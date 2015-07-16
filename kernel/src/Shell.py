import cmd

from Log import Log

class SheelH(cmd.Cmd):
    prompt = "hache@so:~$ "
    intro = "Simple command processor example."
    
    def __init__(self, kernel):
        cmd.Cmd.__init__(self)
        self.kernel = kernel
        
    def do_general(self, arg):
        print(Log().general)
    
    def do_memory(self, arg):
        print(Log().memory)
        
    def do_interruption(self, arg):
        print(Log().interruptions)
        
    def do_cpu(self, arg):
        print(Log().cpu)
        
    def do_io(self, arg):
        print(Log().io)
    
    def do_execute(self, arg):
        if arg:
            self.kernel.run(arg)
        else:
            print("Execute command need a program name")
            
    def do_exit(self, arg):
        print("Stop")
        self.kernel.stop()
        return True