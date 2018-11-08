import os, pkgutil, sys
import transformice
from transformice.packet import incoming
from transformice.utils import Logging
class PacketManager:
    def __init__(self):
        Logging.packet("Loading Packets...")
        self.packets = dict()
        im_package = "incoming"
        im_package_path = os.path.join(os.path.dirname(__file__), im_package.replace(".", "\\"))
        for _, name, __ in pkgutil.iter_modules([im_package_path]):
            package_name = __package__ + "." + im_package + "." + name
            exec("import " + package_name)
            im_modules = sys.modules[package_name]
            for module in dir(im_modules):
                if not module.startswith("IM"): continue
                module_obj = getattr(im_modules, module)
                if incoming.Incoming in module_obj.mro()[1:]:
                    self.__add__(module_obj())
        Logging.packet(f"Packets loaded: {len(self.packets)}")

    def __add__(self, Incoming):
        code = Incoming.tokens[1] + (Incoming.tokens[0] << 8)
        if not self.packets.__contains__(code):
            self.packets[code] = Incoming
            if transformice.debug:
                Logging.packet(f"Packet loaded: {Incoming.tokens}:[{code}]")
        else:
            if transformice.debug:
                print(f"Failed to load Packet: {Incoming.tokens}:[{code}]")

    def __contains__(self, code):
        return self.packets.__contains__(code)

    def get(self, code):
        return self.packets.get(code)