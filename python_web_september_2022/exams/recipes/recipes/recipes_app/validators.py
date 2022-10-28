from django.core import validators


def ingredients_split(value):
    if value in validators.EMPTY_VALUES:
        return []

    list_values = [item.strip() for item in value.split(',') if item.strip()]

    return list_values
