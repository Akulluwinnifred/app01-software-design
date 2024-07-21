from abc import ABC, abstractmethod


class OutputDevice(ABC):
    @abstractmethod
    def output(self) -> str:
        pass


class Monitor(OutputDevice):
    def output(self) -> str:
        return "Monitor output"


class Printer(OutputDevice):
    def output(self) -> str:
        return "Printer output"
