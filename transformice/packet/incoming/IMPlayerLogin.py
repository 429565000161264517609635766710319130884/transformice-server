from transformice.packet import Incoming
from transformice.packet.outgoing.OPEmailAccounts import OPEmailAccounts
from transformice.packet.outgoing.OPIncorrectPassword import OPIncorrectPassword
from transformice.packet.outgoing.OPPlayerIdentification import OPPlayerIdentification
from transformice.game.client.client import Client
class IMPlayerLogin(Incoming):
    tokens = [26, 8]

    def dispatch(self, session, buffer):
        username = buffer.readUTF()
        password = buffer.readUTF()
        access_from = buffer.readUTF()
        initial_room = buffer.readUTF()
        key = buffer.readInt()
        _ = buffer.readByte()
        unknown = buffer.readUTF()

        accounts = session.getAccountsByEmail(username)
        if len(accounts) > 0:
            session.send(OPEmailAccounts(accounts))
            return

        query = "SELECT * FROM accounts WHERE username='{0}' AND password='{1}'".format(username, password)
        session.cursor.execute(query)
        data_exists = False
        # Check if data or user exists in table
        for data in session.cursor:
            if not data is None:
                data_exists = True
        # Check if password or username not wrong
        if data_exists:
            client = Client()
            client.set_session(session)
            client.set_client(session.cursor)
            session.send(OPPlayerIdentification(client))
        else:
            session.send(OPIncorrectPassword())