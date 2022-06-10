def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):
        def area(a, b):
            return a * b

        def perimeter(a, b):
            return 2 * (a + b)

        return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"
    else:
        return ("Enter valid values!")
