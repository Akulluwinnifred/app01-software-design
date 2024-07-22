from typing import Protocol


class Brand(Protocol):
    def set_brand(self) -> str: ...


class Dell(Brand):
    def set_brand(self) -> str:
        return "Brand: Dell"


class IBM(Brand):
    def set_brand(self) -> str:
        return "Brand: IBM"


class HP(Brand):
    def set_brand(self) -> str:
        return "Brand: HP"


class Lenovo(Brand):
    def set_brand(self) -> str:
        return "Brand: Lenovo"
