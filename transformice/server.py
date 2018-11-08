import asyncore, threading, transformice, time
from transformice.network import Network
from transformice.utils.logging import Logging
class Server:
    def __init__(self, host, ports, backlog):
        self.__host = host
        self.__ports = ports
        self.__backlog = backlog
        self.maxConnections = 0
        self.measure = 0

    def start(self):
        host = self.__host
        ports = self.__ports
        backlog = self.__backlog
        onlinePorts = []
        for port in ports:
            try:
                Network(host, port, backlog)
                self.maxConnections += backlog
                onlinePorts.append(port)
            except:
                pass
        if transformice.mysql_pool:
            Logging.mysql(f"MySQL POOL connections: {onlinePorts}")
        thread_name = "transformice-server"
        loop_thread = threading.Thread(target=asyncore.loop, name=thread_name)
        loop_thread.start()
        self.measure = int(round(time.time() * 1000)) - int(round(transformice.started_at * 1000))
        Logging.server(f"Serving on: {onlinePorts}")
        Logging.server(f"Using IP Address: \"{host}\"")
        Logging.server(f"Connection Key:\"{transformice.connkey}\"")
        Logging.server(f"Accepted Version: {transformice.version}")
        Logging.server(f"Max Connections: {transformice.server.maxConnections}")
        Logging.server(f"Started within {self.measure} ms\n")