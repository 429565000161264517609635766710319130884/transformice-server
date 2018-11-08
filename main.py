import transformice

host = '127.0.0.1'
ports = [44444, 44440, 6112, 5555, 3724]
backlog = 300

if __name__ == '__main__':
    transformice.server = transformice.Server(host, ports, backlog)
    transformice.server.start()