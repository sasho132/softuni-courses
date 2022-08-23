from project.table.table import Table


class OutsideTable(Table):
    MIN_TABLE_NUMBER = 51
    MAX_TABLE_NUMBER = 100
    TABLE_TYPE = 'OutsideTable'

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number_error_message(self):
        return f"Outside table's number must be between {self.MIN_TABLE_NUMBER} and {self.MAX_TABLE_NUMBER} inclusive!"
