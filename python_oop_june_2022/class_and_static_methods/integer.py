class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total_sum = 0
        for i in range(len(value) - 1, -1, -1):
            num = roman[value[i]]
            if 3 * num < total_sum:
                total_sum -= num
            else:
                total_sum += num
        return cls(total_sum)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"



first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("III")
print(second_num.value)

print(Integer.from_float(2.6))
print(Integer.from_string("2"))
