from abc import ABC, abstractmethod


class StorageDevice(ABC):
    @abstractmethod
    def store(self) -> str:
        pass

    @abstractmethod
    def retrieve(self) -> str:
        pass


class SSD(StorageDevice):
    def store(self) -> str:
        return "SSD storing data"

    def retrieve(self) -> str:
        return "SSD retrieving data"


class HDD(StorageDevice):
    def store(self) -> str:
        return "HDD storing data"

    def retrieve(self) -> str:
        return "HDD retrieving data"
