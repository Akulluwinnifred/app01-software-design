""
import InputDevice, {Mouse, Keyboard} from "./inputDevices";
import StorageDevice, {SSD, HDD} from "./storageDevices";
import ProcessingDevice, {CPU, GPU} from "./processingDevices";
import OutputDevice, {Monitor, Printer} from "./outputDevices";
import Brand, {IBM,Dell,Hp,Lenovo} from "./brands";


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
abstract class Computer {
    private inputDevice: InputDevice;
    private storageDevice: StorageDevice;
    private processingDevice: ProcessingDevice;
    private outputDevice: OutputDevice;
    public brand: Brand;

    constructor(
        inputDevice: InputDevice,
        storageDevice: StorageDevice,
        processingDevice: ProcessingDevice,
        outputDevice: OutputDevice,
        brand: Brand,
        wifi?: WiFi,
        bluetooth?: Bluetooth
    ) {
        this.inputDevice = inputDevice;
        this.storageDevice = storageDevice;
        this.processingDevice = processingDevice;
        this.outputDevice = outputDevice;
        this.brand = brand;
    }

    abstract manufacturer(): string 

    boot(){
        this.brand.boot();
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

class Desktop extends Computer {
    manufacturer(): string {
        return "Desktop maunfactured by: " + this.brand.setBrand();
    }
}

class Laptop extends Computer implements WiFi, Bluetooth{

    manufacturer(): string {
        return "Laptop maunfactured by: " + this.brand.setBrand();
    }

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
let hp = new Hp();
let lenovo = new Lenovo();



// Desktop does not support WiFi and Bluetooth technologies
// let computer = new Computer(keyboard, ssd, cpu, monitor);
// console.log("========= COMPUTER =================================");
// console.log(computer.Input());      // Outputs: Keyboard input
// computer.setInputDevice(mouse);
// console.log(computer.Input());      // Outputs: Mouse input

// computer.setStorageDevice(hdd);
// console.log(computer.Storage());      // Outputs: HDD input

// console.log(computer.Processing()); // Outputs: CPU processing data
// computer.setProcessingDevice(gpu);
// console.log(computer.Processing()); // Outputs: GPU processing data

// console.log(computer.Output());    // Outputs: Monitor output
// computer.setOutputDevice(printer);
// console.log(computer.Output());




// Laptop supports WiFi and Bluetooth technologies
let laptop = new Laptop(keyboard, ssd, cpu, monitor,hp);
console.log("========= LAPTOP =================================");

laptop.boot()

laptop.setInputDevice(keyboard);
console.log(laptop.Input());      // Outputs: Keyboard input
laptop.setInputDevice(mouse);
console.log(laptop.Input());      // Outputs: Mouse input

laptop.setStorageDevice(ssd);
console.log(laptop.Storage());laptop.setStorageDevice(hdd);
console.log(laptop.Storage());


laptop.setProcessingDevice(cpu);
console.log(laptop.Processing());
laptop.setProcessingDevice(gpu);
console.log(laptop.Processing());

laptop.setOutputDevice(monitor);
console.log(laptop.Output());
laptop.setOutputDevice(printer);
console.log(laptop.Output());

console.log(laptop.connectToWifi());       // Outputs: WiFi connected
console.log(laptop.connectToBluetooth());  // Outputs: Bluetooth connected
console.log(laptop.manufacturer());  

let desktop = new Desktop(keyboard, ssd, cpu, monitor,lenovo);
console.log(desktop.manufacturer()); 