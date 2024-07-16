from abc import ABC, abstractmethod

# Input Components
class InputDevice(ABC):
    @abstractmethod
    def input(self):
        pass

class Keyboard(InputDevice):
    def input(self):
        print("Inputting data from a keyboard...")

class Mouse(InputDevice):
    def input(self):
        print("Inputting data using Mouse...")

class Computer:
    def __init__(self, input_device: InputDevice):
        self.input_device = input_device

    def input(self):
        self.input_device.input()

# Creating instances
keyboard = Keyboard()
mouse = Mouse()
computer_with_keyboard = Computer(keyboard)
computer_with_mouse = Computer(mouse)

# Calling input method
computer_with_keyboard.input()
computer_with_mouse.input()
