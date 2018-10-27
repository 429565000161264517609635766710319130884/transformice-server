from transformice.packet.incoming import Correct_Version
class PacketManager:
    def dispatcher(self, session, token1, token2, buffer):
        if token1 == 28:
            if token2 == 1:
                incoming = Correct_Version()
                incoming.dispatch(session, buffer)

            else:
                print("[INFO][{}, {}] {}".format(token1, token2, buffer.toByteArray()))

        else:
            print("[NEW][{}, {}] {}".format(token1, token2, buffer.toByteArray()))