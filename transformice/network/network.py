import asyncore, socket, transformice
from transformice.network.session import Session
from transformice.utils.logging import Logging
class Network(asyncore.dispatcher):
    def __init__(self, host, port, backlog):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (host, port)
        self.bind(self.address)
        self.listen(backlog)
        # MySQL
        self.mysql = transformice.mysql_pool.get_connection()

    def handle_accepted(self, socket, address):
        Session(socket, self.mysql)

    def handle_close(self):
        self.close()