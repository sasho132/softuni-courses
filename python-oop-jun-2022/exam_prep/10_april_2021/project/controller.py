from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = ["FreshwaterAquarium", "SaltwaterAquarium"]
    VALID_DECORATION_TYPES = ["Ornament", "Plant"]
    VALID_FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."

        aquarium = None
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATION_TYPES:
            return "Invalid decoration type."

        decoration = None
        if decoration_type == "Ornament":
            decoration = Ornament()
        elif decoration_type == "Plant":
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fish = None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        total_price = sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decoration)
        return f"The value of Aquarium {aquarium_name} is {total_price:.2f}."

    def report(self):
        return "\n".join(str(aquarium) for aquarium in self.aquariums)

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None
