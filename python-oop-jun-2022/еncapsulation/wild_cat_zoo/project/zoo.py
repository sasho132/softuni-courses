from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if total_money_for_care <= self.__budget:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [anl for anl in self.animals if isinstance(anl, Lion)]
        tigers = [anl for anl in self.animals if isinstance(anl, Tiger)]
        cheetahs = [anl for anl in self.animals if isinstance(anl, Cheetah)]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result.strip()

    def workers_status(self):
        keepers = [wk for wk in self.workers if isinstance(wk, Keeper)]
        caretakers = [wk for wk in self.workers if isinstance(wk, Caretaker)]
        vets = [wk for wk in self.workers if isinstance(wk, Vet)]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result.strip()
