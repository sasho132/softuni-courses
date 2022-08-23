from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED = 120
    HORSE_INITIAL_SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
