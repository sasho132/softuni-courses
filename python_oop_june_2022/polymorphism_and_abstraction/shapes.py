from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__weight = w

    def calculate_area(self):
        return self.__height * self.__weight

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__weight)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

print(11 * '-')

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
