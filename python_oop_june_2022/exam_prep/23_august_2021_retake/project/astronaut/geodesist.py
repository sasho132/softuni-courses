from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_UNIT_OF_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_UNIT_OF_OXYGEN)
