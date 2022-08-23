from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    FISH_TYPE = None

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decoration = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decoration)

    def add_fish(self, fish):
        if not fish.__class__.__name__ == self.FISH_TYPE:
            return "Water not suitable."
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decoration.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += "Fish: none\n"
        else:
            result += f"Fish: {' '.join(f.name for f in self.fish)}\n"
        result += f"Decorations: {len(self.decoration)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result
