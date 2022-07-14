class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def __search_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__search_by_id(self.customers, customer_id)
        dvd = self.__search_by_id(self.dvds, dvd_id)

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__search_by_id(self.customers, customer_id)
        dvd = self.__search_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"
        return result.strip()
