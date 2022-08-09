from unittest import TestCase
import unittest

from project.mammal import Mammal


class MammalTest(TestCase):
    NAME = 'Name'
    TYPE = 'Type'
    SOUND = 'Sound'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_init_to_be_proper_incremented(self):
        self.assertEqual(self.mammal.name, self.NAME)
        self.assertEqual(self.mammal.type, self.TYPE)
        self.assertEqual(self.mammal.sound, self.SOUND)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_return_proper_info(self):
        expected_result = f"{self.NAME} makes {self.SOUND}"
        actual_result = self.mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_return_proper_info(self):
        expected_result = 'animals'
        actual_result = self.mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)

    def test_info_return_proper_info(self):
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
