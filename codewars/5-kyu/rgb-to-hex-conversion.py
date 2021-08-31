# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    return conv(r) + conv(g) + conv(b)

def conv(val):
    val = clamp(val)
    res = hex(val)[2:]
    if len(res) == 1:
        res = '0' + res
    return res.upper()

def clamp(val):
    return max(0, min(255, val))
