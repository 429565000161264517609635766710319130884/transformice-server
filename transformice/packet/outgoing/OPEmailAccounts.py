from transformice.packet.outgoing import Outgoing
class OPEmailAccounts(Outgoing):
    tokens = [26, 12]

    def __init__(self, accounts):
        self.buffer.writeByte(11)
        data = "¤".join(accounts)
        length = len(data) - 1
        for account in accounts:
            length += 1
        self.buffer.writeShort(length)
        self.buffer.write(data)
        self.buffer.writeUTF("")
