# Program to check if a number is prime or not

num = int(input())

# define a flag variable
number_is_not_prime = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            number_is_not_prime = True
            # break out of loop
            break

# check if flag is True
if number_is_not_prime:
    print('False')
else:
    print('True')
    