""
import InputDevice, {Mouse, Keyboard} from "./inputDevices";
import StorageDevice, {SSD, HDD} from "./storageDevices";
import ProcessingDevice, {CPU, GPU} from "./processingDevices";
import OutputDevice, {Monitor, Printer} from "./outputDevices";



// WiFi & Bluetooth Devices

interface WiFi {
    connectToWifi();
    disconnectFromWiFi();
}

interface Bluetooth {
    connectToBluetooth()
    disconnectFromBluetooth()
}


// The Computer Interface
class Computer {
    private inputDevice: InputDevice;
    private storageDevice: StorageDevice;
    private processingDevice: ProcessingDevice;
    private outputDevice: OutputDevice;

    constructor(
        inputDevice: InputDevice,
        storageDevice: StorageDevice,
        processingDevice: ProcessingDevice,
        outputDevice: OutputDevice,
        wifi?: WiFi,
        bluetooth?: Bluetooth
    ) {
        this.inputDevice = inputDevice;
        this.storageDevice = storageDevice;
        this.processingDevice = processingDevice;
        this.outputDevice = outputDevice;
    }

    setInputDevice(device: InputDevice): void {
        this.inputDevice = device;
    }

    setStorageDevice(device: StorageDevice): void {
        this.storageDevice = device;
    }

    setProcessingDevice(device: ProcessingDevice): void {
        this.processingDevice = device;
    }

    setOutputDevice(device: OutputDevice): void {
        this.outputDevice = device;
    }



    Input(): string {
        return this.inputDevice.input();
    }
    
    Storage(): string {
        return this.storageDevice.store() + " and " + this.storageDevice.retrieve();
    }

    Processing(): string {
        return this.processingDevice.process();
    }

    Output(): string {
        return this.outputDevice.output();
    }

}


class Laptop extends Computer implements WiFi, Bluetooth{

    connectToWifi(): string {
        return "WiFi connected";
    }
    disconnectFromWiFi(): string {
        return "WiFi disconnected";
    }
 
    connectToBluetooth(): string {
        return "Bluetooth connected";
    }
    disconnectFromBluetooth(): string {
        return "Bluetooth disconnected";
    }

}



// Example usage
let keyboard = new Keyboard();
let mouse = new Mouse();
let ssd = new SSD();
let hdd = new HDD();
let cpu = new CPU();
let gpu = new GPU();
let monitor = new Monitor();
let printer = new Printer();



// Desktop does not support WiFi and Bluetooth technologies
let computer = new Computer(keyboard, ssd, cpu, monitor);
console.log("========= COMPUTER =================================");
console.log(computer.Input());      // Outputs: Keyboard input
computer.setInputDevice(mouse);
console.log(computer.Input());      // Outputs: Mouse input
 
computer.setStorageDevice(hdd);
console.log(computer.Storage());      // Outputs: HDD input

console.log(computer.Processing()); // Outputs: CPU processing data
computer.setProcessingDevice(gpu);
console.log(computer.Processing()); // Outputs: GPU processing data

console.log(computer.Output());    // Outputs: Monitor output
computer.setOutputDevice(printer);
console.log(computer.Output());




// Laptop supports WiFi and Bluetooth technologies
let laptop = new Laptop(keyboard, ssd, cpu, monitor);
console.log("========= LAPTOP =================================");
computer.setInputDevice(keyboard);
console.log(computer.Input());      // Outputs: Keyboard input
computer.setInputDevice(mouse);
console.log(computer.Input());      // Outputs: Mouse input

computer.setStorageDevice(ssd);
console.log(computer.Storage());
computer.setStorageDevice(hdd);
console.log(computer.Storage());


computer.setProcessingDevice(cpu);
console.log(computer.Processing());
computer.setProcessingDevice(gpu);
console.log(computer.Processing());

computer.setOutputDevice(monitor);
console.log(computer.Output());
computer.setOutputDevice(printer);
console.log(computer.Output());

console.log(laptop.connectToWifi());       // Outputs: WiFi connected
console.log(laptop.connectToBluetooth());  // Outputs: Bluetooth connected
