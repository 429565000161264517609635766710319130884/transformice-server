from transformice.packet import Outgoing
class OPCaptchaLogin(Outgoing):
    tokens = [26, 20]

    def __init__(self, session, captcha):
        captcha_code, px, ly, lines = captcha
        session.expected_captcha = captcha_code
        self.buffer.writeShort(px)
        self.buffer.writeShort(ly)
        self.buffer.writeShort(px * ly)
        for line in lines:
            self.buffer.writeBytes(b"\x00\x00\x00\x00")
            for value in line.split(","):
                self.buffer.writeByte(value)
                self.buffer.writeBytes(b"\x00\x00\x00")
            self.buffer.writeBytes(b"\x00\x00\x00\x00")
        self.buffer.writeBytes(b"\x00" * int(((px * ly) - (self.buffer.length() - 6) / 4) * 4))