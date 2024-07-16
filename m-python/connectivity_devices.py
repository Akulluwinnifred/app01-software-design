from abc import ABC, abstractmethod



class Wifi(ABC):
    @abstractmethod
    def connect_wifi(self):
        pass


class Bluetooth(ABC):
    @abstractmethod
    def connect_bluetooth(self):
        pass
