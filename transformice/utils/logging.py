class Logging:
    @staticmethod
    def packet(message):
        print(f"[PACKET] {message}")

    @staticmethod
    def error(message):
        print(f"[ERROR] {message}")

    @staticmethod
    def mysql(message):
        print(f"[MYSQL] {message}")

    @staticmethod
    def server(message):
        print(f"[SERVER] {message}")

    @staticmethod
    def session(message):
        print(f"[SESSION] {message}")