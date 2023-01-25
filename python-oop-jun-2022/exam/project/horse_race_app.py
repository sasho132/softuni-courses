from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_VALID_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSE_VALID_TYPES:
            return

        if self.__search_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = None
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__search_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__search_race_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__search_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse_index, horse = self.__search_last_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__search_race_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__search_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__search_race_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __search_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse
        return None

    def __search_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __search_race_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def __search_last_horse_by_type(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[index]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return index, horse
        return -1, None
