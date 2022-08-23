from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_FISH_SIZE = 3
    DEFAULT_FISH_SIZE_INCREASE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_FISH_SIZE, price)
