from abc import ABC, abstractmethod


class Supply(ABC):
    SUPPLY_TYPE = ''

    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_string(value)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__validate_energy(value)
        self.__energy = value

    @staticmethod
    def __validate_string(value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string.")

    @staticmethod
    def __validate_energy(value):
        if 0 > value:
            raise ValueError("Energy cannot be less than zero.")

    def details(self):
        return f"{self.SUPPLY_TYPE}: {self.name}, {self.energy}"
