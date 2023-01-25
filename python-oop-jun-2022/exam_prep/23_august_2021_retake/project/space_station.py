from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.validators import check_valid_astronaut_type


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.non_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        check_valid_astronaut_type(astronaut_type, "Astronaut type is not valid!")

        astronaut = None
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet_items = list(items.split(', '))
        planet = Planet(name)
        planet.items.extend(planet_items)
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")
        planet = self.planet_repository.find_by_name(planet_name)

        astronauts = self.__find_astronauts_for_mission(5, 30)
        if astronauts is None:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_on_mission = 0
        for astro in astronauts:
            if len(planet.items) == 0:
                break
            while astro.oxygen > 0 and len(planet.items) > 0:
                item = planet.items.pop()
                astro.backpack.append(item)
                astro.breathe()
            astronauts_on_mission += 1
            if len(planet.items) == 0:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. {astronauts_on_mission} " \
                       f"astronauts participated in collecting items."
        self.non_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.non_completed_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            result += f"Name: {astro.name}\n"
            result += f"Oxygen: {astro.oxygen}\n"
            if astro.backpack:
                result += f"Backpack items: {', '.join(x for x in astro.backpack)}\n"
            else:
                result += f"Backpack items: none\n"

        return result.strip()

    def __find_astronauts_for_mission(self, count, min_oxygen):
        astronauts = []
        for astro in self.astronaut_repository.astronauts:
            if astro.oxygen > min_oxygen:
                astronauts.append(astro)
        if astronauts:
            filtered_astronauts = sorted(astronauts, key=lambda x: -x.oxygen)[:count]
            return filtered_astronauts
        return None
