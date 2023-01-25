from python_oop_june_2022.testing.list.extended_list import IntegerList

import unittest
from unittest import TestCase


class IntegerListTest(TestCase):

    def test_initialization_without_data(self):
        integers = IntegerList()

        self.assertEqual([], integers._IntegerList__data)

    def test_initialization_with_wrong_types(self):
        integers = IntegerList('abc', 5.5, 3.8)

        self.assertEqual([], integers._IntegerList__data)

    def test_init_with_integers_types(self):
        integers = IntegerList(1, 2, 3)

        self.assertEqual([1, 2, 3], integers._IntegerList__data)

    def test_get_data_expect_to_be_proper(self):
        integers = IntegerList(1, 2, 3)
        expected_result = [1, 2, 3]
        self.assertEqual(expected_result, integers._IntegerList__data)

    def test_add_wrong_type_of_data_expect_raise(self):
        integers = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            integers.add('asd')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_add_correct_type_of_element_expect_to_be_added(self):
        integers = IntegerList(1, 2, 3)
        integers.add(5)
        expected_result = [1, 2, 3, 5]
        self.assertEqual(expected_result, integers._IntegerList__data)

    def test_remove_valid_index_element_expect_to_be_removed(self):
        integers = IntegerList(1, 2, 3)
        integers.remove_index(2)
        expected_result = [1, 2]
        self.assertEqual(expected_result, integers._IntegerList__data)

    def test_remove_invalid_index_raise(self):
        integers = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            integers.remove_index(3)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_remove_index_return_removed_element_on_index(self):
        integers = IntegerList(5)
        result = integers.remove_index(0)
        self.assertEqual(5, result)

    def test_get_index_of_invalid_index_raise(self):
        integers = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            integers.get(3)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_index_return_element_on_index(self):
        integers = IntegerList(1, 2, 3)
        expected_result = integers.get(0)
        self.assertEqual(1, expected_result)

    def test_insert_element_on_invalid_index_raise(self):
        integers = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            integers.insert(3, 1)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_invalid_type_element_on_valid_index_raise(self):
        integers = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            integers.insert(0, 'asd')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_element(self):
        integers = IntegerList(1, 2, 3)
        integers.insert(2, 5)

        self.assertEqual([1, 2, 5, 3], integers.get_data())

    def test_get_biggest_return_biggest_number(self):
        integers = IntegerList(1, 2, 3)
        result = integers.get_biggest()
        expected_result = 3
        self.assertEqual(expected_result, result)

    def test_get_index_return_index_of_element(self):
        integers = IntegerList(1, 2, 3)
        result = integers.get_index(3)
        expected_result = 2
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
