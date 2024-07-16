from input_devices import InputDevice, Keyboard, Mouse
from output_devices import OutputDevice, Monitor, Printer
from storage_devices import StorageDevice, SSD, HDD
from processing_devices import ProcessingDevice, CPU, GPU
from connectivity_devices import Wifi, Bluetooth

class Computer:
    def __init__(
        self,
        inputdevice: InputDevice,
        storageDevice: StorageDevice,
        processingDevice: ProcessingDevice,
        outputdevice: OutputDevice,
        
    ):
        self.inputdevice = inputdevice
        self.storageDevice = storageDevice
        self.processingDevice = processingDevice
        self.outputdevice = outputdevice

    def set_input_device(self, device: InputDevice) -> None:
        self.inputdevice = device

    def set_storage_device(self, device: StorageDevice) -> None:
        self._storage_device = device

    def set_processing_device(self, device: ProcessingDevice) -> None:
        self._processingDevice = device

    def set_output_device(self, device: OutputDevice) -> None:
        self.outputdevice = device

    def input(self) -> str:
        return self.inputdevice.input()

    def storage(self) -> str:
        return f"{self.storageDevice.store_data()} and {self.storageDevice.retrieve_data()}"

    def process(self) -> str:
        return self.processingDevice.process()

    def output(self) -> str:
        return self.outputdevice.output()

class Laptop(Computer,Wifi, Bluetooth):
    def connect_wifi(self):
        print("Connecting to WiFi...") 
    
    def connect_bluetooth(self):
        print("Connecting to Bluetooth...")


keyboard = Keyboard()
mouse = Mouse()
ssd = SSD()
cpu = CPU()
monitor = Monitor()
# wifi = Wifi()
# bluetooth = Bluetooth()
print('================ COMPUTER =====================')
computer = Computer(keyboard, ssd, cpu, monitor)
print(computer.input())
print(computer.storage())
print(computer.process())
print(computer.output())
print('================ LAPTOP =====================')
laptop1 = Laptop(keyboard, ssd, cpu, monitor)
laptop1.connect_wifi()
laptop1.connect_bluetooth()


