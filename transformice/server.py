import asyncore, threading
from transformice.network import Network
class Server:
    def __init__(self, host, ports, backlog):
        self.__host = host
        self.__ports = ports
        self.__backlog = backlog

    def start(self):
        host = self.__host
        ports = self.__ports
        backlog = self.__backlog
        onlinePorts = []
        for port in ports:
            try:
                Network(host, port, backlog)
                onlinePorts.append(port)
            except:
                pass
        thread_name = "transformice-server"
        loop_thread = threading.Thread(target=asyncore.loop, name=thread_name)
        loop_thread.start()
        print("Server running on ports " + str(onlinePorts))