from abc import ABC, abstractmethod


class ProcessingDevice(ABC):
    @abstractmethod
    def process(self) -> str:
        pass


class CPU(ProcessingDevice):
    def process(self) -> str:
        return "CPU processing data"


class GPU(ProcessingDevice):
    def process(self) -> str:
        return "GPU processing data"
