# This is an example of creating different type of functions.

# This function adds as many numbers as we want.
def add_sum(*args):
    return sum(args)


def average_sum(*args):
    return sum(args) / len(args)


print(add_sum(1, 4, 5, 6, 7))
print(average_sum(3, 5, 6, 7, 10, 33))
