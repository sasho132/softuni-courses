from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_UNIT_OF_OXYGEN = 70
    DEFAULT_DECREASING_OXYGEN = 5

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_UNIT_OF_OXYGEN)
