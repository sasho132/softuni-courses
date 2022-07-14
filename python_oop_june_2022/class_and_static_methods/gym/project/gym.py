class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def __search_by_id(self, entities, entity_id):
        return [e for e in entities if e.id == entity_id][0]

    def subscription_info(self, subscription_id):
        subscription = self.__search_by_id(self.subscriptions, subscription_id)
        customer = self.__search_by_id(self.customers, subscription_id)
        trainer = self.__search_by_id(self.trainers, subscription_id)
        equipment = self.__search_by_id(self.equipment, subscription_id)
        plan = self.__search_by_id(self.plans, subscription_id)
        result = f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result
