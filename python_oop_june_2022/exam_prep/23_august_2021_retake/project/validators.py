def check_for_white_space_or_empty_string(value, error_message):
    if not value.strip():
        raise ValueError(error_message)


def check_valid_astronaut_type(astronaut_type, error_message):
    if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
        raise Exception(error_message)

