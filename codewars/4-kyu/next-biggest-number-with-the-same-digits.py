# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    prev = 0
    digits = [int(d) for d in str(n)]
    # Iterate backwards from least to most significant digit.
    for i, current in reversed(list(enumerate(digits))):
        # Find the first digit that is lower than any of the previous digits.
        if current < prev:
            cursor = i + 1
            previous_digits = digits[cursor:]
            # This digit must be swapped with the next largest digit
            # that was encountered during all previous iterations.
            j = i + next_largest_index(current, previous_digits) + 1
            digits[i], digits[j] = digits[j], digits[i]
            # Finally sort the previous digits in ascending order,
            # so that we get the smallest number after the current digit.
            digits[cursor:] = sorted(digits[cursor:])
            return digits_to_int(digits)
        prev = current
    return -1

def next_largest_index(n, digits):
    index, low = None, 10
    for i, d in enumerate(digits):
        if d > n and d < low:
            index, low = i, d
    if index is None:
        raise ValueError('no digit is greater than n')
    return index

def digits_to_int(digits):
    n = 0
    for digit in digits:
        n *= 10
        n += digit
    return n
