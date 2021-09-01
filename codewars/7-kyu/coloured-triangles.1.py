# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111

S = set('RGB')

def combine(a, b):
    if a == b:
        return a
    R = S - set([a, b])
    return list(R)[0]

def reduce(row):
    for i in range(len(row) - 1):
        row[i] = combine(row[i], row[i + 1])
    return row[:-1]

def triangle(row):
    curr = list(row)
    while len(curr) > 1:
        curr = reduce(curr)
    return curr[0]
