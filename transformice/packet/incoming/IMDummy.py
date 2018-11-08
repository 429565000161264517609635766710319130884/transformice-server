from transformice.packet import Incoming
class IMDummy(Incoming):
    tokens = [26, 26]

    def dispatch(self, session, buffer):
        pass