from commons.network.buffer.BufferArray import BufferArray


class Cryptography:
    __packets = []
    __identification = []

    @staticmethod
    def build(packet_keys: list, identification_keys: list):
        Cryptography.__packets = packet_keys
        Cryptography.__identification = identification_keys

    @staticmethod
    def access(auth_key: int, result_key: int):
        for key in Cryptography.__identification:
            auth_key ^= key
        return auth_key == result_key

    # noinspection PyTypeChecker
    @staticmethod
    def identification(data: BufferArray):
        __length = data.readShort()
        __data = []
        while len(__data) < __length:
            __data.append(data.readInt())
        __keys = Cryptography.__key("identification")
        __packet = BufferArray()
        for u32 in Cryptography.__decrypt(__data, -__length, __keys):
            __packet.writeInt(u32)
        return __packet

    @staticmethod
    def message(buffer: BufferArray, pid: int):
        __keys = Cryptography.__key("msg")
        __packet = BufferArray()
        while buffer.available():
            pid = (pid + 1) % len(__keys)
            __packet.writeUnsignedByte((buffer.readUnsignedByte() ^ __keys[pid]) & 0xFF)
        return __packet

    @staticmethod
    def __decrypt(data: list, length: int, key: int):
        __delta = 0x9e3779b9
        __f = Cryptography.__32(data[0])
        if length < 0:
            __length = -length
            __size = Cryptography.__32(6 + 52 // __length)
            __key1 = Cryptography.__32(__size * __delta)
            while __key1 != 0:
                __key2 = Cryptography.__32(__key1 >> 2) & 3
                __p = __length - 1
                while __p >= 0:
                    __l = Cryptography.__32(data[(__length if __p == 0 else __p) - 1])
                    __f = Cryptography.__32(Cryptography.__32(data[__p]) - Cryptography.__bit((Cryptography.__32(__l >> 5) ^ (__f << 2)) + (Cryptography.__32(__f >> 3) ^ (__l << 4)) ^ (__key1 ^ __f) + (key[(__p & 3) ^ __key2] ^ __l)))
                    data[__p] = Cryptography.__32(Cryptography.__bit(__f))
                    __p -= 1
                __key1 = Cryptography.__32(__key1 - __delta)
        return data

    @staticmethod
    def __key(key: str):
        __value = 5381
        for index in range(len(Cryptography.__packets)):
            __value = Cryptography.__32((__value << 5) + __value) + Cryptography.__packets[index] + ord(key[index % len(key)])
        __keys = [-1] * len(Cryptography.__packets)
        for index in range(len(Cryptography.__packets)):
            __value = Cryptography.__bit(__value ^ (__value << 13))
            __value = Cryptography.__bit(__value ^ (__value >> 17))
            __value = Cryptography.__bit(__value ^ (__value << 5))
            __keys[index] = int(__value)
        return __keys

    @staticmethod
    def __32(value: int):
        return value & 0xffffffff

    @staticmethod
    def __bit(value: int):
        return (Cryptography.__32(value) + 2 ** 31) % 2 ** 32 - 2 ** 31
