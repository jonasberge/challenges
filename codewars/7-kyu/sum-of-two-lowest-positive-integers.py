# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    a, b = None, None
    for i, n in enumerate(numbers):
        if   i == 0: a = n
        elif i == 1: b = n
        elif n < a:  a = n
        elif n < b:  b = n
        if i > 0 and a < b:
            # a must always be the larger one,
            # since it should be overwritten first
            # by the above if statement.
            a, b = b, a
    return a + b

