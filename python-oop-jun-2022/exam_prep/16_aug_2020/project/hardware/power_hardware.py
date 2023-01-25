from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    HARDWARE_TYPE = "Power"
    CAPACITY_PERCENT = 0.25
    MEMORY_CAPACITY_PERCENT_INCREASE = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super(PowerHardware, self).__init__(name, self.HARDWARE_TYPE, capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = floor(self.CAPACITY_PERCENT * value)

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = floor(value + (self.MEMORY_CAPACITY_PERCENT_INCREASE * value))
