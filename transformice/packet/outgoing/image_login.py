from transformice.packet.outgoing import Outgoing
class Image_Login(Outgoing):
    tokens = [100, 99]

    def __init__(self, image):
        self.buffer.writeUTF(image)