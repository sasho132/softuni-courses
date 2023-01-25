class StrFromFieldMixin:
    str_fields = ()

    def __str__(self):
        str_fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in str_fields)
