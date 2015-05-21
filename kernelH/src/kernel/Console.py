
class Console:
    def __init__(self):
        self.screen = ""
    
    # Print the message on screen.
    def printMessage(self, message):
        self.screen += message

    # Print the message on screen in lane.
    def printLn(self, message):
        self.screen += (message + "\n")
