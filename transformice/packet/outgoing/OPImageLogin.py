from transformice.packet import Outgoing
class OPImageLogin(Outgoing):
    tokens = [100, 99]

    def __init__(self, image):
        self.buffer.writeUTF(image)