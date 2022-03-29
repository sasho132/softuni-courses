# def calculate_area(width, height):
#     rectangle_area = width * height
#     return rectangle_area

calculate_area = lambda width, height: width * height

a = int(input())
b = int(input())
area = calculate_area(a, b)
print(area)