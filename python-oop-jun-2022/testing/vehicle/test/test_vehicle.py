import unittest
from unittest import TestCase

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    FUEL = 50.0
    CAPACITY = FUEL
    HORSE_POWER = 140.0
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, self.FUEL)
        self.assertEqual(self.vehicle.capacity, self.CAPACITY)
        self.assertEqual(self.vehicle.horse_power, self.HORSE_POWER)
        self.assertEqual(self.vehicle.fuel_consumption, self.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_enough_fuel_reduce_fuel_in_tank(self):
        expected_result = self.vehicle.fuel - (self.vehicle.fuel_consumption * 24)
        self.vehicle.drive(24)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_with_not_enough_fuel_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(60)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_refuel_with_proper_capacity_of_fuel(self):
        self.vehicle.drive(40)
        expected_result = self.vehicle.fuel + 50
        self.vehicle.refuel(50)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_with_more_fuel_quantity_than_tank_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_str_representation(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        actual_result = self.vehicle.__str__()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
