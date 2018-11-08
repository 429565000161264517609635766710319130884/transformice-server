from transformice.packet import Incoming
from transformice.utils.logging import Logging
class IMGameLog(Incoming):
    tokens = [28, 4]

    def dispatch(self, session, buffer):
        error_code1 = buffer.readByte()
        error_code2 = buffer.readByte()
        old_code1 = buffer.readByte()
        old_code2 = buffer.readByte()
        error = buffer.readUTF()
        # Old Error
        if error_code1 == 1 and error_code2 == 1:
            Logging.error(f"[OLD] {old_code1} {old_code2} {error}")
        # Tribulle Error
        elif error_code1 == 60 and error_code2 == 3:
            Logging.error(f"[TRIBULLE] {old_code1} {old_code2} {error}")
        # Protocol Error
        else:
            Logging.error(f"[PROTOCOL] {error_code1} {error_code2} {error}")