import transformice
class Client:
    def __init__(self):
        # Session
        self.session = None
        # String
        self.username = ""
        self.password = ""
        self.email = ""
        # Integer
        self.uid = 0
        self.privilege_level = 0

    def set_session(self, session):
        if self.session is None:
            transformice.client_manager.append(session)
            self.session = session

    def rm_session(self):
        if not self.session is None:
            transformice.client_manager.remove(self.session)
            self.session.disconnect()

    def set_client(self, cursor):
        for (uid, username, email, password, privilege_level) in cursor:
            # User ID
            self.uid = uid
            # User Name
            self.username = username
            # Email
            self.email = email
            # Password
            self.password = password
            # Privilege Level
            self.privilege_level = privilege_level