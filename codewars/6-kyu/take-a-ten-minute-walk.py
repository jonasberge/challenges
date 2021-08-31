# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    minutes = len(walk)
    if minutes != 10:
        return False
    pos = (0, 0)
    dirs = {
        'n': (0, 1),
        'e': (1, 0),
        's': (0, -1),
        'w': (-1, 0),
    }
    for dir in walk:
        offset = dirs[dir]
        pos = tuple(sum(x) for x in zip(pos, offset))
    return pos == (0, 0)
