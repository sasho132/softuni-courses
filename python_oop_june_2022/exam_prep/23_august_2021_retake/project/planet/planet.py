from project.validators import check_for_white_space_or_empty_string


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        check_for_white_space_or_empty_string(
            value, "Planet name cannot be empty string or whitespace!")
        self.__name = value
