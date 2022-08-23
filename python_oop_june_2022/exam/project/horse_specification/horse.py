from abc import ABC, abstractmethod


class Horse(ABC):
    HORSE_MAX_SPEED = None
    HORSE_INITIAL_SPEED_INCREASE = 0

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.HORSE_MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.HORSE_INITIAL_SPEED_INCREASE > self.HORSE_MAX_SPEED:
            self.speed = self.HORSE_MAX_SPEED
        else:
            self.speed += self.HORSE_INITIAL_SPEED_INCREASE
