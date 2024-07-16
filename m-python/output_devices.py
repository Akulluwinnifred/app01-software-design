from abc import ABC, abstractmethod


class OutputDevice(ABC):
    def output(self):
        pass


class Monitor(OutputDevice):
    def output(self):
        return "Monitor outputtting...."

class Printer(OutputDevice):
    def output(self):
        return "Printer outputting...."