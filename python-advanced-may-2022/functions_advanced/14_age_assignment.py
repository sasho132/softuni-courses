def age_assignment(*args, **kwargs):
    persons = {}
    names = args
    pairs = kwargs
    for letter, value in pairs.items():
        for name in names:
            first_letter = name[0]
            if first_letter == letter:
                persons[name] = value
    persons = sorted(persons.items(), key=lambda kv: kv[0])
    result = ''
    for person, age in sorted(persons):
        result += f"{person} is {age} years old.\n"
    return result
