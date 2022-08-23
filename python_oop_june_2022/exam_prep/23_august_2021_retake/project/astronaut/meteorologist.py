from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_UNIT_OF_OXYGEN = 90
    DEFAULT_DECREASING_OXYGEN = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_UNIT_OF_OXYGEN)
