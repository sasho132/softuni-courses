from python_oop_june_2022.testing.cat.cat import Cat

import unittest
from unittest import TestCase


class CatTests(TestCase):
    NAME = 'Cat'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__if_cat_is_already_eaten__expect_rise(self):
        self.cat.eat()
        with self.assertRaises(Exception) as error:
            self.cat.eat()

        self.assertEqual('Already fed.', str(error.exception))

    def test_cat_eat__expect_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat__expect_to_be_sleepy(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_cat_eat__expect_to_increase_size(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_sleep__if_not_fed__expect_rise(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(error.exception))

    def test_sleepy__after_sleep__expect_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
