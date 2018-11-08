import time
from transformice.server import Server
from transformice.network.session import SessionManager
from transformice.packet import PacketManager
from transformice.game.client.manager import ClientManager
from transformice.network.mysql import MySQL

started_at = time.time()
connkey = "xuJxGDUIOofOSf"
version = 480
debug = False
server = None
session_manager = SessionManager()
packet_manager = PacketManager()
client_manager = ClientManager()
mysql_pool =  MySQL().create(name = "transformice-mysql",
                             size = 5,
                             database = "transformice",
                             user = "root",
                             pwd = "abc123",
                             host = "localhost")