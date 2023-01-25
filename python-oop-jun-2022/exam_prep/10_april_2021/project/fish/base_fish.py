from abc import ABC, abstractmethod


class BaseFish(ABC):
    DEFAULT_FISH_SIZE_INCREASE = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name_validation(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__name_validation(value, "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if 0 >= value:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.DEFAULT_FISH_SIZE_INCREASE

    @staticmethod
    def __name_validation(value, error_message):
        if len(value.strip()) == 0:
            raise ValueError(error_message)
