export default interface Brand{
    setBrand(): string;
    boot():void;
}

export class Dell implements Brand {
    setBrand(): string {
        return "Keyboard input";
    }
    boot(){
        console.log("Dell  booting...");
    }

}

export class IBM implements Brand {
    setBrand(): string {
        return "Brand: IBM";
    }
    boot(){
        console.log("IBM  booting...");
    }
}

export class Lenovo implements Brand {
    setBrand(): string {
        return  "Brand: Lenovo";
    }

    boot(){
        console.log("Lenovo  booting...");
    }
}

export class Hp implements Brand {
    setBrand(): string {
        return "Brand: Hp";
    }
    boot(){
        console.log("HP  booting...");
    }
}