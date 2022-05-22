class Vehicle:

    def __init__(self, vehicle_type: str, vehicle_model: str, vehicle_price: int):

        self.vehicle_type = vehicle_type
        self.vehicle_model = vehicle_model
        self.vehicle_price = vehicle_price
        self.owner = None

    def buy(self, money: int, current_owner: str):

        if money >= self.vehicle_price and self.owner is None:
            self.owner = current_owner
            diff = money - self.vehicle_price
            return f"Successfully bought a {self.vehicle_type}. Change: {diff:.2f}"
        elif money < self.vehicle_price:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        elif self.owner is None:
            return "Vehicle has no owner"

    def __repr__(self):

        if self.owner is not None:
            return f"{self.vehicle_model} {self.vehicle_type} is owned by: {self.owner}"
        else:
            return f"{self.vehicle_model} {self.vehicle_type} is on sale: {self.vehicle_price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
