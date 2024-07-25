from typing import Protocol


class Brand(Protocol):
    def boot(self):
        ...

    def set_brand(self) -> str: ...


class Dell(Brand):
    def set_brand(self) -> str:
        return "Brand: Dell"
    
    def boot(self):
        print("Dell booting...")


class IBM(Brand):
    def set_brand(self) -> str:
        return "Brand: IBM"
    
    def boot(self):
        print("IBM booting...")


class HP(Brand):
    def set_brand(self) -> str:
        return "Brand: HP"
    
    def boot(self):
        print("HP booting...")


class Lenovo(Brand):
    def set_brand(self) -> str:
        return "Brand: Lenovo"
    
    def boot(self):
        print("Lenovo booting...")
