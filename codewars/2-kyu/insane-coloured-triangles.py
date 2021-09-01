def combine(a, b):
    if a == b:
        return a
    for l in 'RGB':
        if a != l and b != l:
            return l

def A(n):
    # n = 3^m + 1
    # https://oeis.org/A034472
    from math import log2
    m = log2(n - 1) / log2(3)
    return 3**int(m) + 1

def reduce(row):
    m = A(len(row))
    for i in range(len(row) - m + 1):
        row[i] = combine(row[i], row[i + m - 1])
    return row[:-m + 1]

def triangle(row):
    curr = list(row)
    while len(curr) > 1:
        curr = reduce(curr)
    return curr[0]
