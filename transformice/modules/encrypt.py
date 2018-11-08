from transformice.network.data import Buffer
class Encrypt:
    DELTA = 0x9e3779b9

    @staticmethod
    def u32(arg1):
        return arg1 % 0xFFFFFFFF

    @staticmethod
    def bitMask(arg1):
        return (Encrypt.u32(arg1) + 0x80000000) % 0x100000000 - 0x80000000

    @staticmethod
    def MX(z, y, sum, k, p, e):
        return ((z >> 5 ^ y << 2) + (y >> 3 ^ z << 4) ^ (sum ^ y) + (k[(p & 3) ^ e] ^ z))

    @staticmethod
    def getKeys(key):
        keys =  [18, 21, 44, 14, 39, 37, 48, 41, 44, 19, 83, 120, 120, 83, 76, 75, 118, 84, 113, 115]
        loc3 = 0
        loc4 = len(keys)
        loc5 = len(key)
        loc6 = 5381
        while loc3 < loc4:
            loc6 = Encrypt.bitMask((loc6 << 5) + loc6 + keys[loc3] + ord(key[loc3 % loc5]))
            loc3 += 1
        loc3 = 0
        found = [0]*loc4
        while loc3 < loc4:
            loc6 ^= Encrypt.bitMask(loc6 << 13)
            loc6 ^= Encrypt.bitMask(loc6 >> 17)
            loc6 ^= Encrypt.bitMask(loc6 << 5)
            found[loc3] = int(loc6)
            loc3 += 1
        return found

    @staticmethod
    def decryptMessage(buffer, packetid):
        pid = packetid
        keys = Encrypt.getKeys("msg")
        data = Buffer()
        while data.length() > 0:
            pid = (pid + 1) % len(keys)
            data.writeByte(buffer.readByte() ^ keys[pid])
        return data

    @staticmethod
    def rawDecrypt(v, n, k):
        q = 6 + 52 // n
        sum = q * Encrypt.DELTA
        y = v[0]
        while sum != 0:
            e = (sum >> 2) & 3
            p = n - 1
            while p >= 0:
                z = Encrypt.u32(v[(n if p == 0 else p) - 1])
                v[p] -= Encrypt.MX(z, y, sum, k, p, e)
                y = Encrypt.u32(v[p])
                p -= 1
            sum -= Encrypt.DELTA
        return v

    @staticmethod
    def decryptPacket(buffer):
        ldata = buffer.readShort()
        idata = []
        while len(idata) < ldata:
            idata.append(buffer.readInt())
        keys = Encrypt.getKeys("identification")
        idata = Encrypt.rawDecrypt(idata, ldata, keys)
        data = Buffer()
        x = 0
        while x < len(idata):
            data.writeInt(idata[x])
            x += 1
        return data