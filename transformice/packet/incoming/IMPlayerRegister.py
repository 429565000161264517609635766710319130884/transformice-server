from transformice.packet.incoming import Incoming
from transformice.utils.logging import Logging
from transformice.game.client.client import Client
class IMPlayerRegister(Incoming):
    tokens = [26, 7]

    def dispatch(self, session, buffer):
        username = buffer.readUTF()
        password = buffer.readUTF()
        email = buffer.readUTF()
        captcha = buffer.readUTF()
        key = buffer.readUTF()
        access_from = buffer.readUTF()

        # MySQL
        registered = session.checkRegistered(username, password)
        if registered:
            return

        # Get Last User ID
        last_id = session.getLastPlayerId()
        if last_id is None:
            last_id = 1
        else:
            last_id += 1

        session.getAccountsByEmail(email)

        add_user = ("INSERT INTO accounts"
                    "(id, username, email, password, privilege) "
                    "VALUES (%(userid)s, %(username)s, %(email)s, %(password)s, %(privilege)s)")

        data_user = {
            'userid': last_id,
            'username': username,
            'email': email,
            'password': password,
            'privilege': 1
        }

        session.cursor.execute(add_user, data_user)
        session.mysql.commit()

        # Create Client
        client = Client()
        # Attr Session to Client
        client.set_session(session)