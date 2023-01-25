from project.drink.drink import Drink


class Water(Drink):
    INITIAL_WATER_PRICE = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.INITIAL_WATER_PRICE, brand)
