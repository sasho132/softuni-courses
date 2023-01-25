from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    FISH_TYPE = "FreshwaterFish"
    INITIAL_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)
