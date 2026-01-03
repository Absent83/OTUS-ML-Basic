"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(
        self,
        weight: float = 0.0,
        fuel: float = 0.0,
        fuel_consumption: float = 0.0,
    ):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance: float):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel()
