from abc import ABC, abstractmethod
from input_device import InputDevice, Keyboard, Mouse
from storage_device import StorageDevice, SSD, HDD
from processing_device import ProcessingDevice, CPU, GPU
from output_device import OutputDevice, Monitor, Printer
from wifi_device import WiFiDevices
from bluetooth_device import BluetoothDevices


# Define Computer class
class Computer:
    def __init__(
        self,
        input_device: InputDevice,
        storage_device: StorageDevice,
        processing_device: ProcessingDevice,
        output_device: OutputDevice,
    ):
        self._input_device = input_device
        self._storage_device = storage_device
        self._processing_device = processing_device
        self._output_device = output_device

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


# Laptop extends Computer and implements wifi and Bluetooth interfaces
class Laptop(Computer, WiFiDevices, BluetoothDevices):

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


computer = Computer(keyboard, ssd, cpu, monitor)
print("=================Computer===============")
print(computer.input())  # Outputs: Keyboard input
print(computer.storage())  # Outputs: SSD storing data and SSD retrieving data
print(computer.processing())  # Outputs: CPU processing data
print(computer.output())  # Outputs: Monitor output
# Change the input device
computer.set_input(mouse)
print(computer.input())  # Outputs: Mouse input
# Create a computer without WiFi and Bluetooth support


Laptop1 = Laptop(keyboard, ssd, cpu, monitor)

print("=================Laptop===============")
print(Laptop1.connectToBluetooth())  # Outputs: Bluetooth connected
print(Laptop1.disconnectFromBluetooth())  # Outputs: Bluetooth disconnected
print(Laptop1.connectToWifi())  # Outputs: WiFi connected
print(Laptop1.disconnectFromWifi())  # Outputs:WiFi disconnected
