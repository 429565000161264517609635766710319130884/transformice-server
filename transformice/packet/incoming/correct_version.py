from transformice.packet.incoming import Incoming
from transformice.packet.outgoing import Correct_Version as Out_Version
from transformice.packet.outgoing import Banner_Login, Image_Login
class Correct_Version(Incoming):
    tokens = [28, 1]

    def dispatch(self, session, buffer):
        version = buffer.readShort()
        connkey = buffer.readUTF()
        session.send(Out_Version(session.expected_pid))
        session.send(Image_Login("x_cimetiere.jpg"))
        session.send(Banner_Login(23))