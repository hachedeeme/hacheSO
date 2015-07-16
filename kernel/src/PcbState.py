
class PcbState:
    def __init__(self):
        self.state
        raise NotImplementedError("Can't create a PcbState object'")
    
    def __str__(self):
        return self.state

class New(PcbState):
    def __init__(self):
        self.state = 'NEW'

class Ready(PcbState):
    def __init__(self):
        self.state = 'READY'

class Running(PcbState):
    def __init__(self):
        self.state = 'RUNNING'
        
class Finish(PcbState):
    def __init__(self):
        self.state = 'FINISH'
        
class IOState(PcbState):
    def __init__(self):
        self.state = 'IO'