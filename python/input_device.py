from abc import ABC, abstractmethod


# Define interfaces
class InputDevice(ABC):
    @abstractmethod
    def input(self) -> str:
        pass


class Keyboard(InputDevice):
    def input(self) -> str:
        return "Keyboard input"


class Mouse(InputDevice):
    def input(self) -> str:
        return "Mouse input"
