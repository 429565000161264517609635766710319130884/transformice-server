from transformice.packet.outgoing import Outgoing
class OPIncorrectPassword(Outgoing):
    tokens = [26, 12]

    def __init__(self):
        self.buffer.writeByte(2)
        self.buffer.writeUTF("")
        self.buffer.writeUTF("")