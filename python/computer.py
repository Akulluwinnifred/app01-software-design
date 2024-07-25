from abc import ABC, abstractmethod
from input_device import InputDevice, Keyboard, Mouse
from storage_device import StorageDevice, SSD, HDD
from processing_device import ProcessingDevice, CPU, GPU
from output_device import OutputDevice, Monitor, Printer
from wifi_device import WiFiDevices
from bluetooth_device import BluetoothDevices
from brands import Dell, IBM, Lenovo, HP, Brand


# Define Computer class
class Computer(ABC):
    def __init__(
        self,
        input_device: InputDevice,
        storage_device: StorageDevice,
        processing_device: ProcessingDevice,
        output_device: OutputDevice,
        brand: Brand,
    ):
        self._input_device = input_device
        self._storage_device = storage_device
        self._processing_device = processing_device
        self._output_device = output_device
        self.brand = brand

    @abstractmethod
    def manufacture(self) -> str:
        pass

    def boot(self):
        self.brand.boot()
    
    def set_input(self, device: InputDevice) -> None:
        self._input_device = device

    def set_storage(self, device: StorageDevice) -> None:
        self._storage_device = device

    def set_processing(self, device: ProcessingDevice) -> None:
        self._processing_device = device

    def set_output(self, device: OutputDevice) -> None:
        self._output_device = device

    def input(self) -> str:
        return self._input_device.input()

    def storage(self) -> str:
        return f"{self._storage_device.store()} and {self._storage_device.retrieve()}"

    def processing(self) -> str:
        return self._processing_device.process()

    def output(self) -> str:
        return self._output_device.output()


# Refinned Abstractions


class DesktopComputer(Computer):
    def manufacture(self):
        return f"Desktop Manufactured by the  {self.brand.set_brand()}"


class WalltopComputer(Computer):
    def manufacture(self):
        return f"Walltop Manufactured by the  {self.brand.set_brand()}"


class TabletComputer(Computer):
    def manufacture(self):
        return f"Tablet Manufactured by the  {self.brand.set_brand()}"


class PalmtopComputer(Computer):
    def manufacture(self):
        return f"Palmtop Manufactured by the  {self.brand.set_brand()}"


# Laptop extends Computer and implements wifi and Bluetooth interfaces
class Laptop(Computer, WiFiDevices, BluetoothDevices):

    def manufacture(self):
        return f"Laptop Manufactured by the  {self.brand.set_brand()}"

    def connectToBluetooth(self) -> str:
        return "Bluetooth connected"

    def disconnectFromBluetooth(self) -> str:
        return "Bluetooth disconnected"

    def connectToWifi(self) -> str:
        return "WiFi connected"

    def disconnectFromWifi(self) -> str:
        return "WiFi disconnected"


# Example usage
keyboard = Keyboard()
mouse = Mouse()
ssd = SSD()
cpu = CPU()
monitor = Monitor()


# computer = Computer(keyboard, ssd, cpu, monitor)
# print("=================Computer===============")
# print(computer.input())  # Outputs: Keyboard input
# print(computer.storage())  # Outputs: SSD storing data and SSD retrieving data
# print(computer.processing())  # Outputs: CPU processing data
# print(computer.output())  # Outputs: Monitor output
# # Change the input device
# computer.set_input(mouse)
# print(computer.input())  # Outputs: Mouse input
# # Create a computer without WiFi and Bluetooth support


Laptop1 = Laptop(keyboard, ssd, cpu, monitor, Dell())
Laptop2 = Laptop(keyboard, ssd, cpu, monitor, Lenovo())
Laptop3 = Laptop(keyboard, ssd, cpu, monitor, HP())
Laptop4 = Laptop(keyboard, ssd, cpu, monitor, IBM())
Laptop4.boot()

walltop1 = WalltopComputer(keyboard, ssd, cpu, monitor, Lenovo())
walltop2 = WalltopComputer(keyboard, ssd, cpu, monitor, Dell())
walltop3 = WalltopComputer(keyboard, ssd, cpu, monitor, IBM())
walltop4 = WalltopComputer(keyboard, ssd, cpu, monitor, HP())
walltop4.boot()

palmtop1 = PalmtopComputer(keyboard, ssd, cpu, monitor, IBM())
palmtop2 = PalmtopComputer(keyboard, ssd, cpu, monitor, Dell())
palmtop3 = PalmtopComputer(keyboard, ssd, cpu, monitor, HP())
palmtop4 = PalmtopComputer(keyboard, ssd, cpu, monitor, Lenovo())
palmtop4.boot()

desktop1 = DesktopComputer(keyboard, ssd, cpu, monitor, HP())
desktop2 = DesktopComputer(keyboard, ssd, cpu, monitor, Dell())
desktop3 = DesktopComputer(keyboard, ssd, cpu, monitor, IBM())
desktop4 = DesktopComputer(keyboard, ssd, cpu, monitor, Lenovo())
desktop2.boot()

print("=================Laptop===============")
print(Laptop1.manufacture())
print(Laptop2.manufacture())
print(Laptop3.manufacture())
print(Laptop4.manufacture())
print("")

print("=================Walltop===============")
print(walltop1.manufacture())
print(walltop2.manufacture())
print(walltop3.manufacture())
print(walltop4.manufacture())
print("")

print("=================Palmtop===============")
print(palmtop1.manufacture())
print(palmtop2.manufacture())
print(palmtop3.manufacture())
print(palmtop4.manufacture())
print("")

print("=================Desktop===============")
print(desktop1.manufacture())
print(desktop2.manufacture())
print(desktop3.manufacture())
print(desktop4.manufacture())
print("")
