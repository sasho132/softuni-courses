first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')

# Create list for each of the rows
row_one_list = list(map(int, first_row))
row_two_list = list(map(int, second_row))
row_tree_list = list(map(int, third_row))

# Create list for each of the three columns
column_one = [row_one_list[0], row_two_list[0], row_tree_list[0]]
column_two = [row_one_list[1], row_two_list[1], row_tree_list[1]]
column_three = [row_one_list[2], row_two_list[2], row_tree_list[2]]

# Create list for each of the two diagonals
x1 = [row_one_list[0], row_two_list[1], row_tree_list[2]]
x2 = [row_one_list[2], row_two_list[1], row_tree_list[0]]

if row_one_list.count(2) == 3 or row_two_list.count(2) == 3 or row_tree_list.count(2) == 3 or column_one.count(2) == 3\
        or column_one.count(2) == 3 or column_one.count(
        2) == 3 or x1.count(2) == 3 or x2.count(2) == 3:
    print("Second player won")
elif row_one_list.count(1) == 3 or row_two_list.count(1) == 3 or row_tree_list.count(1) == 3\
        or column_one.count(1) == 3 or column_one.count(1) == 3 or column_one.count(1) == 3 or x1.count(1) == 3\
        or x2.count(1) == 3:
    print('First player won')
else:
    print('Draw!')
