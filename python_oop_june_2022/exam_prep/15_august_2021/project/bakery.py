from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if self.__find_food_by_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if self.__find_drink_by_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.__find_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__find_first_valid_table(number_of_people)
        if table is None:
            return f"No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        foods_in_the_menu = []
        foods_not_in_the_menu = []

        for food_name in food_names:
            food = self.__find_food_by_name(food_name)
            if food is None:
                foods_not_in_the_menu.append(food_name)
            else:
                table.order_food(food)
                foods_in_the_menu.append(food)

        result = ''
        result += f"Table {table_number} ordered:\n"
        for food in foods_in_the_menu:
            result += repr(food) + '\n'
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join([f for f in foods_not_in_the_menu])
        return result.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        drinks_in_the_menu = []
        drinks_not_in_the_menu = []

        for drink_name in drink_names:
            drink = self.__find_drink_by_name(drink_name)
            if drink is None:
                drinks_not_in_the_menu.append(drink_name)
            else:
                table.order_drink(drink)
                drinks_in_the_menu.append(drink)

        result = ''
        result += f"Table {table_number} ordered:\n"
        for drink in drinks_in_the_menu:
            result += repr(drink) + '\n'
        result += f"{self.name} does not have in the menu:\n"
        result += '\n'.join([f for f in drinks_not_in_the_menu])
        return result.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()

        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if table.free_table_info() is not None:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def __find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return None

    def __find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def __find_first_valid_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                return table
        return None
