from project.table.table import Table


class InsideTable(Table):
    MIN_TABLE_NUMBER = 1
    MAX_TABLE_NUMBER = 50
    TABLE_TYPE = 'InsideTable'

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number_error_message(self):
        return f"Inside table's number must be between {self.MIN_TABLE_NUMBER} and {self.MAX_TABLE_NUMBER} inclusive!"
