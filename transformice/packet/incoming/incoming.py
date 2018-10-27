from abc import abstractmethod
class Incoming:
    tokens = []
    @abstractmethod
    def dispatch(self, session, buffer):
        raise NotImplementedError