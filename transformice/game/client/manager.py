class ClientManager:
    def __init__(self):
        self.__clients = []

    def append(self, client):
        self.__clients.append(client)

    def remove(self, client):
        self.__clients.remove(client)

    def pos_by_uid(self, uid):
        i = 0
        while len(self.__clients) > i:
            if self.__clients[i].uid == uid:
                return i
            i += 1