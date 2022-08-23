from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    INITIAL_PORTION_SIZE = 245.0

    def __init__(self, name: str, price: float):
        super().__init__(name, self.INITIAL_PORTION_SIZE, price)
