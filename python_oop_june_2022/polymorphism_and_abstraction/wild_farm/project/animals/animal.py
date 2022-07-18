from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def food_type(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    def feed(self, food: Food):
        food_give = food.__class__.__name__
        animal_type = self.__class__.__name__
        if food_give not in self.food_type:
            return f"{animal_type} does not eat {food_give}!"
        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, " \
               f"{self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, " \
               f"{self.living_region}, {self.food_eaten}]"
