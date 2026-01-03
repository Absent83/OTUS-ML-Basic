"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):

    def __init__(
        self,
        weight: float = 0.0,
        fuel: float = 0.0,
        fuel_consumption: float = 0.0,
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
