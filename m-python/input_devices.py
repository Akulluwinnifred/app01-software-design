from abc import ABC, abstractmethod

class InputDevice(ABC):
    @abstractmethod
    def input(self) -> str:
        pass

class Keyboard(InputDevice):
    def input(self):
        return "Keyboard inputting...."

class Mouse(InputDevice):
    def input(self):
        return "Mouse inputting...."