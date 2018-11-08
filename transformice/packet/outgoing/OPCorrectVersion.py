import random
from transformice.packet import Outgoing
class OPCorrectVersion(Outgoing):
    tokens = [26, 3]

    def __init__(self, last_pid):
        self.buffer.writeInt(0)
        self.buffer.writeByte(last_pid)
        self.buffer.writeUTF("BR")
        self.buffer.writeUTF("BR")
        self.buffer.writeInt(random.randrange(0xFFFF))