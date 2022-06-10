def concatenate(*args, **kwargs):
    result_string = ''
    for word in args:
        result_string += word

    for key, value in kwargs.items():
        old_word = key
        new_word = value
        if old_word in result_string:
            result_string = result_string.replace(old_word, new_word)

    return result_string
