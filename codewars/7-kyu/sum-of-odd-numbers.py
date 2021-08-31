# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    # Count the number of elements of all previous rows.
    elements = n*(n-1)//2 # 1 + 2 + ... + n-1
    # Determine the first element of the target row.
    first_in_row = 2*elements+1
    # Sum the first element n times and add 2
    # for the 1st element, 4 for the 2nd, etc.,
    # i.e. 2 * (1 + 2 + ... + n-1)
    total = n*first_in_row + 2*elements
    return total
