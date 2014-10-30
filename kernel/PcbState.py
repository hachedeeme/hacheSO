class State:
    def __init__(self):
        raise NotImplementedError("Can't create a State object'")


class New(State):
    def __init__(self):
        self.state = ''


class Ready(State):
    def __init__(self):
        self.state = ''


class Running(State):
    def __init__(self):
        self.state = ''