from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    DEFAULT_COMFORT = 1
    DEFAULT_PRICE = 5.0

    def __init__(self):
        super().__init__(self.DEFAULT_COMFORT, self.DEFAULT_PRICE)
