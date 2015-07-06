
class PcbState:
    def __init__(self):
        raise NotImplementedError("Can't create a PcbState object'")

class New(PcbState):
    def __init__(self):
        self.state = ''


class Ready(PcbState):
    def __init__(self):
        self.state = ''

class Running(PcbState):
    def __init__(self):
        self.state = ''
        
class Finish(PcbState):
    def __init__(self):
        self.state = ''
        
class IOState(PcbState):
    def __init__(self):
        self.state = ''