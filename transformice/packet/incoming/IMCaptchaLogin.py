from transformice.packet import Incoming
from transformice.packet.outgoing.OPCaptchaLogin import OPCaptchaLogin
from transformice.utils import utils
class IMPlayerLogin(Incoming):
    tokens = [26, 20]

    def dispatch(self, session, buffer):
        session.send(OPCaptchaLogin(session, utils.getCaptcha()))