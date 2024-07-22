export default interface InputDevice {
    input(): string;
}

export class Keyboard implements InputDevice {
    input(): string {
        return "Keyboard input";
    }
}

export class Mouse implements InputDevice {
    input(): string {
        return "Mouse input";
    }
}
