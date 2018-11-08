import mysql.connector.pooling
from transformice.utils.logging import Logging
class MySQL:
    @staticmethod
    def create(**kwargs):
        Logging.mysql("Trying to connect MySQL POOL...")
        cnx = None
        try:
            cnx = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = kwargs["name"],
                pool_size = kwargs["size"],
                database = kwargs["database"],
                user = kwargs["user"],
                password = kwargs["pwd"],
                host = kwargs["host"]
            )
        except mysql.connector.PoolError as e:
            Logging.mysql("Pool Error: " + str(e))
        except Exception as e:
            Logging.mysql("Exception: " + str(e))
        return cnx