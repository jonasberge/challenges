# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    bs = set(b)
    return [n for n in a if n not in bs]
