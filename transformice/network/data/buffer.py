from struct import pack, unpack
class Buffer:
    def __init__(self, data = b''):
        if type(data) == str:
            self.bytes = data.encode()
        elif type(data) == bytes:
            self.bytes = data
        else:
            self.bytes = b''

    def toByteArray(self):
        return self.bytes

    def toString(self):
        return self.bytes.decode()

    def length(self):
        return len(self.bytes)

    def readable(self):
        return len(self.bytes) > 0

    def clear(self):
        self.bytes = b''

    def write(self, data):
        self.bytes += data.encode()

    def writeBytes(self, data):
        self.bytes += data

    def writeBool(self, data):
        self.bytes += pack('!?', bool(data))

    def writeByte(self, data):
        self.bytes += pack('!B', int(data))

    def writeShort(self, data):
        self.bytes += pack('!H', int(data))

    def writeInt24(self, data):
        self.bytes += pack('!B', int(data) >> 16 % 255)
        self.bytes += pack('!B', int(data) >> 8 % 255)
        self.bytes += pack('!B', int(data) % 255)

    def writeInt(self, data):
        self.bytes += pack('!I', int(data))

    def writeLong(self, data):
        self.bytes += pack('!Q', int(data))

    def writeUTF(self, data):
        self.writeShort(len(data))
        self.write(data)

    def read(self, length):
        data = self.bytes[:length]
        self.bytes = self.bytes[length:]
        return data.decode()

    def readBytes(self, length):
        return self.read(length).encode()

    def readBool(self):
        data = unpack('!?', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return bool(data)

    def readByte(self):
        data = unpack('!B', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return int(data)

    def readShort(self):
        data = unpack('!H', self.bytes[:2])[0]
        self.bytes = self.bytes[2:]
        return int(data)

    def readInt24(self):
        data = unpack('!B', self.bytes[:1])[0] << 16
        data |= unpack('!B', self.bytes[:1])[0] << 8
        data |= unpack('!B', self.bytes[:1])[0]
        self.bytes = self.bytes[3:]
        return int(data)

    def readInt(self):
        data = unpack('!I', self.bytes[:4])[0]
        self.bytes = self.bytes[4:]
        return int(data)

    def readLong(self):
        data = unpack('!Q', self.bytes[:8])[0]
        self.bytes = self.bytes[8:]
        return int(data)

    def readUTF(self):
        length = self.readShort()
        data = self.read(length)
        return data
