from project.software.software import Software


class ExpressSoftware(Software):
    SOFTWARE_TYPE = "Express"
    MEMORY_CONSUMPTION_INCREASE = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super(ExpressSoftware, self).__init__(name, self.SOFTWARE_TYPE, capacity_consumption, memory_consumption)

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = value * self.MEMORY_CONSUMPTION_INCREASE
