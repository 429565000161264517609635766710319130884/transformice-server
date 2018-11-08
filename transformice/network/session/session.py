import asyncore
import transformice
from transformice.network.data import *
from transformice.utils.logging import Logging
class Session(asyncore.dispatcher):
    out_buffer = b''
    def __init__(self, socket, mysql):
        super().__init__(socket)
        # Session Manager
        transformice.session_manager.append(self)
        # MySQL
        self.mysql = mysql
        self.cursor = mysql.cursor()
        # Session Properties
        self.address = ""
        self.connected = True
        self.client = None
        self.expected_pid = 0
        self.excepted_captcha = ""
        self.current_language = 0
        # Connection Made
        self.handle_connect()

    def disconnect(self):
        if not self.connected:
            return

        transformice.session_manager.remove(self)
        self.connected = False
        self.close()

    def handle_connect(self):
        self.address = self.socket.getpeername()[0]
        Logging.session(f"Connection on IP: \"{self.address}\"")

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
        pid = buffer.readByte()
        if not self.expected_pid == pid:
            self.disconnect()
            return
        self.expected_pid = (self.expected_pid + 1) % 100

        # Tokens
        token1 = buffer.readByte()
        token2 = buffer.readByte()
        opcodes = token2 + (token1 << 8)

        # Packet Manager
        if transformice.packet_manager.__contains__(opcodes):
            transformice.packet_manager.get(opcodes).dispatch(self, buffer)
        else:
            Logging.packet(f"[NOT FOUND] [{token1}, {token2}] => {opcodes} | {buffer.toByteArray()}")

    def send(self, data):
        data = Encoder.encode(data)
        if transformice.debug:
            Logging.session(f"\"{self.address}\" SENT: {data}")
        self.socket.send(data)

    def handle_close(self):
        self.disconnect()

    def checkRegistered(self, username, password):
        registered = False
        get_user = ("SELECT * FROM accounts "
                    "WHERE username = %s "
                    "AND password = %s")
        data_user = (username, password)
        self.cursor.execute(get_user, data_user)
        for data in self.cursor:
            if data is not None:
                registered = False
            else:
                registered = True
        return registered

    def getLastPlayerId(self):
        self.cursor.execute("SELECT MAX(id) FROM accounts;")
        for (last_id,) in self.cursor:
            return last_id

    def getAccountsByEmail(self, email):
        accounts = []
        query = "SELECT username FROM accounts WHERE email = '{0}';".format(email)
        self.cursor.execute(query)
        for (username,) in self.cursor:
            accounts.append(username)
        return accounts