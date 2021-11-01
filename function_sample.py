# This is an example of creating different type of functions.

# This function adds as many numbers as we want.
def add_sum(*args):
    return sum(args)

# This function does a average of multiple arguments being passed into the function


def average_sum(*args):
    return sum(args) / len(args)

# This is a function that take 2 arguments.


def two_number_average(a, b):
    return a + b


print(add_sum(1, 4, 5, 6, 7))
print(average_sum(3, 5, 6, 7, 10, 33))
print(two_number_average(1, 7))
