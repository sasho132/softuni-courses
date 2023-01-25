from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    NAME = 'Name'
    CAPACITY = 10

    def test_init(self):
        train = Train(self.NAME, self.CAPACITY)
        self.assertEqual(self.NAME, train.name)
        self.assertEqual(self.CAPACITY, train.capacity)
        self.assertListEqual([], train.passengers)

    def test_add_with_full_capacity_raise(self):
        train = Train(self.NAME, self.CAPACITY)
        for passenger in range(10):
            train.passengers.append(f"Name{passenger}")
        with self.assertRaises(ValueError) as error:
            train.add('Test')
        expected_error = "Train is full"
        self.assertEqual(expected_error, str(error.exception))

    def test_add_with_existing_passenger_name_rise(self):
        train = Train(self.NAME, self.CAPACITY)
        passenger_name = 'TestName'
        train.passengers.append(passenger_name)
        with self.assertRaises(ValueError) as error:
            train.add('TestName')
        expected_error = f"Passenger {passenger_name} Exists"
        self.assertEqual(expected_error, str(error.exception))

    def test_add_with_proper_passenger_name_and_capacity_expect_to_be_added(self):
        train = Train(self.NAME, self.CAPACITY)
        passengers_name = 'TestName'
        actual_result = train.add(passengers_name)
        expected_message = f"Added passenger {passengers_name}"
        self.assertEqual(expected_message, actual_result)
        self.assertListEqual(["TestName"], train.passengers)

    def test_remove_not_existing_passenger_rise(self):
        train = Train(self.NAME, self.CAPACITY)
        passengers_name = 'TestName'
        with self.assertRaises(ValueError) as error:
            train.remove(passengers_name)
        expected_error_message = "Passenger Not Found"
        self.assertEqual(expected_error_message, str(error.exception))

    def test_remove_existing_passenger_expect_to_be_removed(self):
        train = Train(self.NAME, self.CAPACITY)
        passengers_name = 'TestName'
        train.passengers.append(passengers_name)
        actual_result = train.remove(passengers_name)
        expected_message = f"Removed {passengers_name}"
        self.assertEqual(actual_result, expected_message)
        self.assertListEqual([], train.passengers)


if __name__ == "__main__":
    main()
