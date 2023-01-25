def even_odd_filter(**kwargs):
    for even_odd, value in kwargs.items():
        if even_odd == 'even':
            value = [x for x in value if x % 2 == 0]
            kwargs[even_odd] = value
        else:
            value = [x for x in value if x % 2 != 0]
            kwargs[even_odd] = value
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    result = {}
    for key, value in sorted_kwargs:
        result[key] = value
    return result
