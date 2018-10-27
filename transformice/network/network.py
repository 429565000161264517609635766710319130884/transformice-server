import asyncore, socket
from transformice.network.session import Session
class Network(asyncore.dispatcher):
    def __init__(self, host, port, backlog):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(backlog)

    def handle_accepted(self, socket, address):
        Session(socket)

    def handle_close(self):
        self.close()