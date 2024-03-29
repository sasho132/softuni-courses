from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    FISH_TYPE = "SaltwaterFish"
    INITIAL_CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)
