from transformice.packet import Outgoing
class OPBannerLogin(Outgoing):
    tokens = [16, 9]

    def __init__(self, id):
        self.buffer.writeByte(1)
        self.buffer.writeByte(id)
        self.buffer.writeBool(True)
        self.buffer.writeBool(False)