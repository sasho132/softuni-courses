import unittest
from unittest import TestCase

from python_oop_june_2022.testing.car_manager.car_manager import Car


class CarTests(TestCase):
    MAKE = 3
    MODEL = 'Model'
    FUEL_CONSUMPTION = 5
    FUEL_CAPACITY = 50
    FUEL_AMOUNT = 0

    def setUp(self) -> None:
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    def test_init_expect_to_be_proper(self):
        self.assertEqual(self.car.make, self.MAKE)
        self.assertEqual(self.car.model, self.MODEL)
        self.assertEqual(self.car.fuel_consumption, self.FUEL_CONSUMPTION)
        self.assertEqual(self.car.fuel_capacity, self.FUEL_CAPACITY)
        self.assertEqual(self.car.fuel_amount, self.FUEL_AMOUNT)


if __name__ == "__main__":
    unittest.main()
