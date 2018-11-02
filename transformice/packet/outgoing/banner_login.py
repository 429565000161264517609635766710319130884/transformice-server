from transformice.packet.outgoing import Outgoing
class Banner_Login(Outgoing):
    tokens = [16, 9]

    def __init__(self, id):
        self.buffer.writeByte(1)
        self.buffer.writeByte(id)
        self.buffer.writeBool(True)
        self.buffer.writeBool(False)