S = set('RGB')

def combine(a, b):
    if a == b:
        return a
    R = S - set([a, b])
    return list(R)[0]

def reduce(row):
    for i in range(len(row) - 1):
        row[i] = combine(row[i], row[i + 1])
    # print(''.join(row[:-1]))
    return row[:-1]

def triangle(row):
    # print(row)
    curr = list(row)
    while len(curr) > 1:
        curr = reduce(curr)
    return curr[0]

# =====

import random
from collections import defaultdict

# test.assert_equals(triangle('GB'), 'R')
# test.assert_equals(triangle('RRR'), 'R')
# test.assert_equals(triangle('RGBG'), 'B')
# test.assert_equals(triangle('RBRGBRB'), 'G')
# test.assert_equals(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
# test.assert_equals(triangle('B'), 'B')

"""
test.assert_equals(triangle('RRRRRRRRR'), 'X')
test.assert_equals(triangle('RRRRRRRRG'), 'X')
test.assert_equals(triangle('RRRRRRRGR'), 'X')
test.assert_equals(triangle('RRRRRRGRR'), 'X')
test.assert_equals(triangle('RRRRRGRRR'), 'X')
"""

s = set('RGB')
pairs = ['RG', 'GB', 'BR']

def generate(n):
    return ''.join(random.choice(list(s)) for _ in range(n))

def reverse(s):
    return ''.join(list(reversed(s)))

def counter(s, c):
    x = '#'
    r = reverse(s)
    a, b = tuple(c)
    r = r.replace(a, x)
    r = r.replace(b, a)
    r = r.replace(x, b)
    return r

"""
for _ in range(10):
    N = 10
    a = generate(10)
    c = defaultdict(lambda: 0)
    for ax in a:
        c[ax] += 1
    t = triangle(a)
    print('.', dict(c))
    print(a)
    print(t)
    print()
"""

"""
for x in ['RB', 'BG', 'GR']:
    for i in range(100):
        l = ''.join(random.choice(list(s)) for _ in range(40))
        r = counter(l, x)
        actual = triangle(l + r)
        expected = list(s - set(x))[0]
        test.assert_equals(actual, expected)
        print(l, r, actual, expected)
"""

"""
for i in range(10):
    a = generate(10)
    b = generate(10)
    for pair in pairs:
        ax = counter(a, pair)
        bx = counter(b, pair)
        u = triangle(a + ax)
        v = triangle(bx + b)
        print(pair, '-', u, v)
    print(triangle(a + b))
    print()
"""


"""
print(triangle('BGBGGGBRRG'))
print(triangle('BGRGGGBRRG'))
print(triangle('BGGGGGBRRG'))
print()

print(triangle('BGRRRGBRRG'))
print(triangle('BGBBBGBRRG'))
print()

# replace the middle G of the three G's -> identical result
print(triangle('BGBGGGBRRG'))
print(triangle('BGBGBGBRRG'))
print(triangle('BGBGRGBRRG'))
print()

# replace the first R of the last dual R -> identical result
print(triangle('BGBGGGBRRG'))
print(triangle('BGBGGGBBRG'))
print(triangle('BGBGGGBGRG'))
print()

# replace the last R of the last dual R -> identical result
print(triangle('BGBGGGBRRG'))
print(triangle('BGBGGGBRBG'))
print(triangle('BGBGGGBRGG'))
print()
"""

"""
for length in range(2, 1000):
    is_ok = True
    for _ in range(16):
        x = generate(length)
        t = triangle(x)
        a, b = x[0], x[-1]
        if t != combine(a, b):
            is_ok = False
            break
    if is_ok:
        print(length)
"""
