"""
Examples of using homework_05 classes.
"""

from homework_05.car import Car
from homework_05.plane import Plane
from homework_05.engine import Engine
from homework_05.exceptions import LowFuelError, NotEnoughFuel, CargoOverload


def example_car():
    """Working with Car and Engine."""
    car = Car(weight=1500, fuel=50, fuel_consumption=0.1)

    engine = Engine(volume=2.0, pistons=4)
    car.set_engine(engine)

    print(f"Car weight: {car.weight}")
    print(f"Engine: {car.engine}")

    car.start()
    print(f"Car started: {car.started}")

    car.move(100)
    print(f"Fuel after 100km: {car.fuel}")


def example_plane():
    """Working with Plane and cargo."""
    plane = Plane(weight=5000, fuel=1000, fuel_consumption=0.5, max_cargo=2000)

    plane.load_cargo(500)
    plane.load_cargo(1000)
    print(f"Current cargo: {plane.cargo}")

    removed = plane.remove_all_cargo()
    print(f"Removed cargo: {removed}, current: {plane.cargo}")


def example_low_fuel_error():
    """LowFuelError when starting without fuel."""
    car = Car(weight=1500, fuel=0, fuel_consumption=0.1)

    try:
        car.start()
    except LowFuelError:
        print("Cannot start: no fuel")


def example_not_enough_fuel():
    """NotEnoughFuel when moving too far."""
    car = Car(weight=1500, fuel=10, fuel_consumption=0.1)
    car.start()

    try:
        car.move(200)  # needs 20, has 10
    except NotEnoughFuel:
        print("Cannot move: not enough fuel")


def example_cargo_overload():
    """CargoOverload when loading too much."""
    plane = Plane(weight=5000, fuel=1000, fuel_consumption=0.5, max_cargo=100)

    try:
        plane.load_cargo(150)
    except CargoOverload:
        print("Cannot load: cargo overload")


if __name__ == "__main__":
    print("=== Car example ===")
    example_car()

    print("\n=== Plane example ===")
    example_plane()

    print("\n=== LowFuelError example ===")
    example_low_fuel_error()

    print("\n=== NotEnoughFuel example ===")
    example_not_enough_fuel()

    print("\n=== CargoOverload example ===")
    example_cargo_overload()
