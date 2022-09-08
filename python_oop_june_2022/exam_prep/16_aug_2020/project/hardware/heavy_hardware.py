from math import floor

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    HARDWARE_TYPE = "Heavy"
    CAPACITY_INCREASE_VALUE = 2
    MEMORY_CAPACITY_PERCENT = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super(HeavyHardware, self).__init__(name, self.HARDWARE_TYPE, capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = self.CAPACITY_INCREASE_VALUE * value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = floor(self.MEMORY_CAPACITY_PERCENT * value)
