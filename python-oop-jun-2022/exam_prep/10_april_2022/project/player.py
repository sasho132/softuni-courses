class Player:
    player_names = []
    MIN_STAMINA = 0
    MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        Player.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__validate_stamina(value)
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < Player.MAX_STAMINA

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @staticmethod
    def __validate_name(value):
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in Player.player_names:
            raise Exception(f"Name {value} is already used!")

    @staticmethod
    def __validate_age(value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

    @staticmethod
    def __validate_stamina(value):
        if Player.MIN_STAMINA > value or value > Player.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
