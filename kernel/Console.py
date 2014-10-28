class Console:
    def __init__(self):
        self.screen = ""

    def printMessage(self, message):
        self.screen += message

    def printLn(self, message):
        self.screen += (message + "\n")
