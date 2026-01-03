"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(
        self,
        weight: float = 0.0,
        fuel: float = 0.0,
        fuel_consumption: float = 0.0,
        max_cargo: float = 0.0,
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0.0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: float):
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload()
        self.cargo += cargo

    def remove_all_cargo(self) -> float:
        cargo = self.cargo
        self.cargo = 0.0
        return cargo
