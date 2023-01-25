from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    @property
    def food_type(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_increase(self):
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    @property
    def food_type(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    @property
    def food_type(self):
        return ['Vegetable', 'Meat']

    @property
    def weight_increase(self):
        return 0.30


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    @property
    def food_type(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 1
