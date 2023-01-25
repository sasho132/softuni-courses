from python_oop_june_2022.testing.worker.worker import Worker
import unittest
from unittest import TestCase


class WorkerTest(TestCase):
    NAME = 'Name'
    SALARY = 300
    ENERGY = 100
    MONEY = 0

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_worker__init__expect_to_be_proper(self):
        self.assertEqual(self.worker.name, self.NAME)
        self.assertEqual(self.worker.salary, self.SALARY)
        self.assertEqual(self.worker.energy, self.ENERGY)
        self.assertEqual(self.worker.money, self.MONEY)

    def test_rest__expect_to_be_incremented(self):
        self.worker.rest()
        expected_return = self.ENERGY + 1

        self.assertEqual(self.worker.energy, expected_return)

    def test_worker__tries_to_work_with_zero_energy__expect_rise(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as error:
            worker.work()

        self.assertEqual('Not enough energy.', str(error.exception))

    def test_after_work__expect_money_increased_by_his_salary(self):
        self.worker.work()

        expected_return = self.MONEY + self.SALARY
        self.assertEqual(self.worker.money, expected_return)

    def test_after_work__expect_energy_to_decrease(self):
        self.worker.work()

        expected_return = self.ENERGY - 1
        self.assertEqual(self.worker.energy, expected_return)

    def test_get_info__expect_proper_string(self):
        self.assertEqual(self.worker.get_info(), f'{self.NAME} has saved {self.MONEY} money.')


if __name__ == '__main__':
    unittest.main()
