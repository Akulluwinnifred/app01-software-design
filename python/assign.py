from abc import ABC, abstractmethod

# Input Components interface
class InputDevice(ABC):
    @abstractmethod
    def input(self):
        pass

# Keyboard class implementing InputDevice
class Keyboard(InputDevice):
    def input(self):
        print("Inputing data from a keyboard...")

# Mouse class implementing InputDevice
class Mouse(InputDevice):
    def input(self):
        print("Inputing data using Mouse...")

# Storage Devices interface
class StorageDevice(ABC):
    @abstractmethod
    def store(self, data):
        pass

    @abstractmethod
    def retrieve(self):
        pass

# SSD class implementing StorageDevice
class SSD(StorageDevice):
    def store(self, data):
        print(f"Storing data in SSD: {data}")

    def retrieve(self):
        print("Retrieving data from SSD")

# HDD class implementing StorageDevice
class HDD(StorageDevice):
    def store(self, data):
        print(f"Storing data in HDD: {data}")

    def retrieve(self):
        print("Retrieving data from HDD")

# Processing Devices interface
class ProcessingDevice(ABC):
    @abstractmethod
    def process(self, data):
        pass

# CPU class implementing ProcessingDevice
class CPU(ProcessingDevice):
    def process(self, data):
        print(f"Processing data using CPU: {data}")

# GPU class implementing ProcessingDevice
class GPU(ProcessingDevice):
    def process(self, data):
        print(f"Processing data using GPU: {data}")

# Output Devices interface
class OutputDevice(ABC):
    @abstractmethod
    def output(self, data):
        pass

# Monitor class implementing OutputDevice
class Monitor(OutputDevice):
    def output(self, data):
        print(f"Outputting data to Monitor: {data}")

# Printer class implementing OutputDevice
class Printer(OutputDevice):
    def output(self, data):
        print(f"Outputting data to Printer: {data}")

# WiFi interface
class WiFi:
    def connect(self):
        print("Connected to WiFi")

    def disconnect(self):
        print("Disconnected from WiFi")

# Bluetooth interface
class Bluetooth:
    def connect(self):
        print("Connected to Bluetooth")

    def disconnect(self):
        print("Disconnected from Bluetooth")

# Computer class
class Computer:
    def __init__(self, input_device, storage_device, processing_device, output_device, wifi=None, bluetooth=None):
        self.input_device = input_device
        self.storage_device = storage_device
        self.processing_device = processing_device
        self.output_device = output_device
        self.wifi = wifi
        self.bluetooth = bluetooth

    def input(self):
        self.input_device.input()

    def store_data(self, data):
        self.storage_device.store(data)

    def process_data(self, data):
        self.processing_device.process(data)

    def output_data(self, data):
        self.output_device.output(data)

    def connect_wifi(self):
        if self.wifi:
            self.wifi.connect()

    def disconnect_wifi(self):
        if self.wifi:
            self.wifi.disconnect()

    def connect_bluetooth(self):
        if self.bluetooth:
            self.bluetooth.connect()

    def disconnect_bluetooth(self):
        if self.bluetooth:
            self.bluetooth.disconnect()

# Desktop class extending Computer
class Desktop(Computer):
    def behave_like_a_desktop(self):
        pass

# Laptop class extending Computer
class Laptop(Computer):
    def save_battery(self):
        pass

# Create instances
keyboard = Keyboard()
mouse = Mouse()
ssd = SSD()
cpu = CPU()
monitor = Monitor()
wifi = WiFi()
bluetooth = Bluetooth()

computer = Computer(keyboard, ssd, cpu, monitor, wifi, bluetooth)

# Call input method
computer.input()

# Set new input device and call input method again
computer.input_device = mouse
computer.input()

# Set back to keyboard and call input method again
computer.input_device = keyboard
computer.input()

# Store data
computer.store_data("Hello, World!")

# Process data
computer.process_data("Hello, World!")

# Output data
computer.output_data("Hello, World!")

# Connect/Disconnect WiFi
computer.connect_wifi()
computer.disconnect_wifi()

# Connect/Disconnect Bluetooth
computer.connect_bluetooth()
computer.disconnect_bluetooth()
