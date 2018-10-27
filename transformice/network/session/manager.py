class SessionManager:
    def __init__(self):
        self.__sessions = []

    def append(self, session):
        self.__sessions.append(session)

    def remove(self, session):
        self.__sessions.remove(session)