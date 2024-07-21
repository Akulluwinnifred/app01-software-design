from abc import ABC, abstractmethod


class BluetoothDevices(ABC):
    def connectToBluetooth(self) -> str:
        pass

    def disconnectFromBluetooth(self) -> str:
        pass
