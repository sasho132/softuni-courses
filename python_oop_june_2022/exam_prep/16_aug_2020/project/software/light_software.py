from math import floor

from project.software.software import Software


class LightSoftware(Software):
    SOFTWARE_TYPE = "Light"
    CAPACITY_PERCENT_MORE = 0.5
    MEMORY_PERCENT_LESS = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super(LightSoftware, self).__init__(name, self.SOFTWARE_TYPE, capacity_consumption, memory_consumption)

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        self.__capacity_consumption = floor(value + (value * self.CAPACITY_PERCENT_MORE))

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = floor(value - (value * self.MEMORY_PERCENT_LESS))
