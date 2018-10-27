from transformice.packet.incoming import Incoming
from transformice.packet.outgoing import Correct_Version as Out_Version
class Correct_Version(Incoming):
    tokens = [28, 1]

    def dispatch(self, session, buffer):
        version = buffer.readShort()
        connkey = buffer.readUTF()
        session.send(Out_Version(session.expected_pid))