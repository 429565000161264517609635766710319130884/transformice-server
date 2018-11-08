import transformice
from transformice.packet.outgoing import Outgoing
class OPPlayerIdentification(Outgoing):
    tokens = [26, 2]

    def __init__(self, client):
        """
            \x05\xdd*\xe2\x00\x0bKinash#5616\x00\x00\x10m\x03\x00(\r\x83\x01\x00\x00
            this._SafeStr_3413 = _arg_1.readInt(); \x05\xdd*\xe2\x00
            this._SafeStr_848 = _arg_1.readUTF(); x00\x0bKinash#5616
            this._SafeStr_3622 = _arg_1.readInt(); \x00\x00\x10m
            this._SafeStr_3606 = _arg_1.readByte(); \x03
            this._SafeStr_872 = _arg_1.readInt(); \x00(\r\x83
            this._SafeStr_3623 = _arg_1.readBoolean(); \x01
            var _local_2:int = _arg_1.readByte(); \x00
            this._SafeStr_3624 = new Vector.<int>();
            var _local_3:int = _SafeStr_11959._SafeStr_9342;
            while (_local_3 < _local_2) 1 < 0
            {
                this._SafeStr_3624.push(_arg_1.readByte());
                _local_3++;
            };
            this._SafeStr_3625 = _arg_1.readBoolean(); \x00
        """
        self.buffer.writeInt(client.uid)
        self.buffer.writeUTF(client.username)
        self.buffer.writeInt(client.uid)
        self.buffer.writeByte(client.session.current_language.value)
        self.buffer.writeInt(2624899)
        self.buffer.writeBool(True)
        self.buffer.writeByte(client.privilege_level)
        self.buffer.writeBool(False)