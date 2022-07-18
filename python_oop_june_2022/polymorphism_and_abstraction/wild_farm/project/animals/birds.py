from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def food_type(self):
        return ['Meat']

    @property
    def weight_increase(self):
        return 0.25


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    @property
    def food_type(self):
        return ['Vegetable', 'Fruit', 'Meat', 'Seed']

    @property
    def weight_increase(self):
        return 0.35
