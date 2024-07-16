"";
"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var inputDevices_1 = require("./inputDevices");
var storageDevices_1 = require("./storageDevices");
var processingDevices_1 = require("./processingDevices");
var outputDevices_1 = require("./outputDevices");
// The Computer Interface
var Computer = /** @class */ (function () {
    function Computer(inputDevice, storageDevice, processingDevice, outputDevice, wifi, bluetooth) {
        this.inputDevice = inputDevice;
        this.storageDevice = storageDevice;
        this.processingDevice = processingDevice;
        this.outputDevice = outputDevice;
    }
    Computer.prototype.setInputDevice = function (device) {
        this.inputDevice = device;
    };
    Computer.prototype.setStorageDevice = function (device) {
        this.storageDevice = device;
    };
    Computer.prototype.setProcessingDevice = function (device) {
        this.processingDevice = device;
    };
    Computer.prototype.setOutputDevice = function (device) {
        this.outputDevice = device;
    };
    Computer.prototype.Input = function () {
        return this.inputDevice.input();
    };
    Computer.prototype.Storage = function () {
        return this.storageDevice.store() + " and " + this.storageDevice.retrieve();
    };
    Computer.prototype.Processing = function () {
        return this.processingDevice.process();
    };
    Computer.prototype.Output = function () {
        return this.outputDevice.output();
    };
    return Computer;
}());
var Laptop = /** @class */ (function (_super) {
    __extends(Laptop, _super);
    function Laptop() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Laptop.prototype.connectToWifi = function () {
        return "WiFi connected";
    };
    Laptop.prototype.disconnectFromWiFi = function () {
        return "WiFi disconnected";
    };
    Laptop.prototype.connectToBluetooth = function () {
        return "Bluetooth connected";
    };
    Laptop.prototype.disconnectFromBluetooth = function () {
        return "Bluetooth disconnected";
    };
    return Laptop;
}(Computer));
// Example usage
var keyboard = new inputDevices_1.Keyboard();
var mouse = new inputDevices_1.Mouse();
var ssd = new storageDevices_1.SSD();
var hdd = new storageDevices_1.HDD();
var cpu = new processingDevices_1.CPU();
var gpu = new processingDevices_1.GPU();
var monitor = new outputDevices_1.Monitor();
var printer = new outputDevices_1.Printer();
// Desktop does not support WiFi and Bluetooth technologies
var computer = new Computer(keyboard, ssd, cpu, monitor);
console.log("========= COMPUTER =================================");
console.log(computer.Input()); // Outputs: Keyboard input
computer.setInputDevice(mouse);
console.log(computer.Input()); // Outputs: Mouse input
computer.setStorageDevice(hdd);
console.log(computer.Storage()); // Outputs: HDD input
console.log(computer.Processing()); // Outputs: CPU processing data
computer.setProcessingDevice(gpu);
console.log(computer.Processing()); // Outputs: GPU processing data
console.log(computer.Output()); // Outputs: Monitor output
computer.setOutputDevice(printer);
console.log(computer.Output());
// Laptop supports WiFi and Bluetooth technologies
var laptop = new Laptop(keyboard, ssd, cpu, monitor);
console.log("========= LAPTOP =================================");
computer.setInputDevice(keyboard);
console.log(computer.Input()); // Outputs: Keyboard input
computer.setInputDevice(mouse);
console.log(computer.Input()); // Outputs: Mouse input
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
console.log(laptop.connectToWifi()); // Outputs: WiFi connected
console.log(laptop.connectToBluetooth()); // Outputs: Bluetooth connected
