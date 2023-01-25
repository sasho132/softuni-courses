from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_FISH_SIZE_INCREASE = 2
    DEFAULT_FISH_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_FISH_SIZE, price)
