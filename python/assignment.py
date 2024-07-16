from abc import ABC, abstractmethod

# Define interfaces
class InputDevice(ABC):
    @abstractmethod
    def input(self) -> str:
        pass

class StorageDevice(ABC):
    @abstractmethod
    def store(self) -> str:
        pass

    @abstractmethod
    def retrieve(self) -> str:
        pass

class ProcessingDevice(ABC):
    @abstractmethod
    def process(self) -> str:
        pass

class OutputDevice(ABC):
    @abstractmethod
    def output(self) -> str:
        pass
class WiFiDevices(ABC):
    def connectToWifi(self) -> str:
        pass
    
    def disconnectFromWifi(self) -> str:
        pass
class BluetoothDevices(ABC):
    def connectToBluetooth(self) -> str:
        pass
    
    def disconnectFromBluetooth(self) -> str:
        pass    

class Keyboard(InputDevice):
    def input(self) -> str:
        return "Keyboard input"

class Mouse(InputDevice):
    def input(self) -> str:
        return "Mouse input"

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

class CPU(ProcessingDevice):
    def process(self) -> str:
        return "CPU processing data"

class GPU(ProcessingDevice):
    def process(self) -> str:
        return "GPU processing data"

class Monitor(OutputDevice):
    def output(self) -> str:
        return "Monitor output"

class Printer(OutputDevice):
    def output(self) -> str:
        return "Printer output"



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
       
    def set_input_device(self, device: InputDevice) -> None:
        self._input_device = device

    def set_storage_device(self, device: StorageDevice) -> None:
        self._storage_device = device

    def set_processing_device(self, device: ProcessingDevice) -> None:
        self._processing_device = device

    def set_output_device(self, device: OutputDevice) -> None:
        self._output_device = device

    
    def perform_input(self) -> str:
        return self._input_device.input()

    def perform_storage(self) -> str:
        return f"{self._storage_device.store()} and {self._storage_device.retrieve()}"

    def perform_processing(self) -> str:
        return self._processing_device.process()

    def perform_output(self) -> str:
        return self._output_device.output()

    def connect_wifi(self) -> str:
        if self._wifi:
            return self._wifi.connect()
        return "No WiFi support"

    def connect_bluetooth(self) -> str:
        if self._bluetooth:
            return self._bluetooth.connect()
        return "No Bluetooth support"
    


#Laptop extends Computer and implements wifi and Bluetooth interfaces
class Laptop(Computer, WiFiDevices , BluetoothDevices) :
    
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
print(computer.perform_input())      # Outputs: Keyboard input
print(computer.perform_storage())    # Outputs: SSD storing data and SSD retrieving data
print(computer.perform_processing()) # Outputs: CPU processing data
print(computer.perform_output())     # Outputs: Monitor output
# Change the input device
computer.set_input_device(mouse)
print(computer.perform_input())      # Outputs: Mouse input
# Create a computer without WiFi and Bluetooth support




Laptop1=Laptop(keyboard, ssd, cpu, monitor)
print(Laptop1.connectToBluetooth())  # Outputs: Bluetooth connected
print(Laptop1.disconnectFromBluetooth())  # Outputs: Bluetooth disconnected
print(Laptop1.connectToWifi())  # Outputs: WiFi connected
print(Laptop1.disconnectFromWifi()) # Outputs:WiFi disconnected
from abc import ABC, abstractmethod

