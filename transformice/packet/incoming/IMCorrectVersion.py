import transformice
from transformice.packet import Incoming
from transformice.packet.outgoing.OPCorrectVersion import OPCorrectVersion
from transformice.packet.outgoing.OPBannerLogin import OPBannerLogin
from transformice.packet.outgoing.OPImageLogin import OPImageLogin
from transformice.utils.logging import Logging
class IMCorrectVersion(Incoming):
    tokens = [28, 1]

    def dispatch(self, session, buffer):
        version = buffer.readShort()
        connkey = buffer.readUTF()
        session.send(OPCorrectVersion(session.expected_pid))
        session.send(OPImageLogin("x_cimetiere.jpg"))
        session.send(OPBannerLogin(23))
        if transformice.debug:
            Logging.session(f"[CONNECTION] {version} && {connkey}")