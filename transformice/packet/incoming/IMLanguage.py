from transformice.packet import Incoming
import transformice
class IMLanguage(Incoming):
    tokens = [8, 2]

    def dispatch(self, session, buffer):
        language_code = buffer.readByte()
        session.current_language = transformice.utils.Language(language_code)