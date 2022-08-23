from abc import ABC, abstractmethod
from project.validators import check_for_white_space_or_empty_string


class Astronaut(ABC):
    DEFAULT_DECREASING_OXYGEN = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        check_for_white_space_or_empty_string(
            value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.DEFAULT_DECREASING_OXYGEN

    def increase_oxygen(self, amount):
        self.oxygen += amount
