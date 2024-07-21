from abc import ABC, abstractmethod


class WiFiDevices(ABC):
    def connectToWifi(self) -> str:
        pass

    def disconnectFromWifi(self) -> str:
        pass
