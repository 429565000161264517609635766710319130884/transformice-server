import asyncore
import transformice
from transformice.network.data import *
class Session(asyncore.dispatcher):
    out_buffer = b''
    def __init__(self, socket):
        super().__init__(socket)
        # Session Manager
        transformice.session_manager.append(self)
        # Session Properties
        self.connected = True
        self.client = None
        self.expected_pid = 0

    def disconnect(self):
        if not self.connected:
            return

        transformice.session_manager.remove(self)
        self.connected = False
        self.close()

    def handle_read(self):
        if not self.connected:
            return

        self.out_buffer = self.recv(1024)

        if not self.out_buffer:
            return

        # Policy File Request
        if self.out_buffer[0] == 60 and self.client == None:
            self.send('<cross-domain-policy><allow-access-from domain="*" to-ports="*" /></cross-domain-policy>\x00')
            self.disconnect()
            return

        # Transformice Packet
        buffer = Buffer(self.out_buffer)
        length = buffer.readByte()

        if length == 1:
            buffer.readByte()
        elif length == 2:
            buffer.readShort()
        elif length == 3:
            buffer.readInt24()
        else:
            return

        # Packet ID Verification
        packet_id = buffer.readByte()
        if not self.expected_pid == packet_id:
            self.disconnect()
            return
        self.expected_pid = (self.expected_pid + 1) % 100

        # Tokens
        token1 = buffer.readByte()
        token2 = buffer.readByte()

        # Packet Manager
        transformice.packet_manager.dispatcher(self, token1, token2, buffer)

    def send(self, data):
        data = Encoder.encode(data)
        print("SENT: " + str(data))
        print(self.socket)
        self.socket.send(data)

    def handle_close(self):
        self.disconnect()