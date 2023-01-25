import unittest
from unittest import TestCase

from project.plantation import Plantation


class PlantationTests(TestCase):
    SIZE = 2

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.plantation.size, self.SIZE)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_init_with_negative_size_number_rise(self):
        with self.assertRaises(ValueError) as error:
            plantation = Plantation(-10)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_already_hired_worker_rise(self):
        self.plantation.hire_worker('Worker')

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Worker')

        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker_add_worker_proper(self):
        worker = 'Worker'
        result = self.plantation.hire_worker(worker)
        self.assertEqual(self.plantation.workers, ['Worker'])
        self.assertEqual(f"{worker} successfully hired.", result)

    def test_len_method(self):
        self.plantation.plants['Worker1'] = ['test1']
        self.plantation.plants["Worker2"] = ['test2']
        expected_result = 2
        actual_result = self.plantation.__len__()

        self.assertEqual(expected_result, actual_result)

    def test_planting_with_not_existing_worker_raise(self):
        worker = 'Worker'

        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, 'Tomato')

        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

    def test_planting_with_full_plantation_raise(self):
        self.plantation.hire_worker('Worker')
        self.plantation.hire_worker('Worker2')
        self.plantation.planting('Worker', 'Tomato')
        self.plantation.planting('Worker2', 'test')

        with self.assertRaises(ValueError) as error:
            self.plantation.planting('Worker', 'test')

        self.assertEqual("The plantation is full!", str(error.exception))

    def test_planting_worker_with_first_plant_expect_plant_to_be_added_to_plants(self):
        worker = 'Worker'
        plant = 'plant'
        self.plantation.hire_worker(worker)
        result = self.plantation.planting(worker, plant)
        self.assertEqual(f"{worker} planted it's first {plant}.", result)
        self.assertEqual(self.plantation.plants[worker], ['plant'])

    def test_planting_worker_with_already_planted_plant(self):
        worker = 'Worker'
        plant = 'plant'
        plant2 = 'plant2'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant)
        result = self.plantation.planting(worker, plant2)
        self.assertEqual(f"{worker} planted {plant2}.", result)
        self.assertEqual(self.plantation.plants[worker], ['plant', 'plant2'])

    def test_str_representation(self):
        worker = 'Worker'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, 'test')

        expected_result = f"Plantation size: {self.SIZE}\n{worker}\n{worker} planted: test"
        actual_result = self.plantation.__str__()

        self.assertEqual(expected_result, actual_result)

    def test_repr(self):
        worker = 'Worker'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, 'test')

        expected_result = f'Size: {self.plantation.size}\nWorkers: {worker}'
        actual_result = self.plantation.__repr__()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
