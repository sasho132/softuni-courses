class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    @property
    def dvd_names(self):
        return [m.name for m in self.rented_dvds]

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(self.dvd_names)})"
