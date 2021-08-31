# https://www.codewars.com/kata/546e2562b03326a88e000020

import math

def digits(num):
    if num < 0:
        raise 'num cannot be negative'
    if num == 0:
        return 1
    return math.floor(math.log10(num)) + 1

def square_digits(num):
    res, mul = 0, 1
    for i in range(digits(num)):
        digit = num % 10
        num //= 10
        square = digit**2
        res += mul * square
        mul *= 10**digits(square)
    return res
