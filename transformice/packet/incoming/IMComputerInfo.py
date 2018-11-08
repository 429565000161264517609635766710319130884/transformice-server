from transformice.packet import Incoming
class IMComputerInfo(Incoming):
    tokens = [28, 17]

    def dispatch(self, session, buffer):
        pass