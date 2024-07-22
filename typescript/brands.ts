export default interface Brand{
    setBrand(): string;
}

export class Dell implements Brand {
    setBrand(): string {
        return "Keyboard input";
    }
}

export class IBM implements Brand {
    setBrand(): string {
        return "Brand: IBM";
    }
}

export class Lenovo implements Brand {
    setBrand(): string {
        return  "Brand: Lenovo";
    }
}

export class Hp implements Brand {
    setBrand(): string {
        return "Brand: Hp";
    }
}