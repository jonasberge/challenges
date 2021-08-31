# https://www.codewars.com/kata/5277c8a221e209d3f6000b56

from collections import deque

open_close = {
    '(': ')',
    '[': ']',
    '{': '}',
}
close_open = {
    v: k for k, v in open_close.items()
}
pairs = {
    **open_close,
    **close_open,
}

def opening(b): return b in open_close
def closing(b): return b in close_open

def matching(a, b):
    return pairs[a] == b

def validBraces(string):
    stack = deque()
    for brace in string:
        if opening(brace):
            stack.append(brace)
        elif closing(brace):
            if len(stack) == 0:
                return False
            other = stack.pop()
            if not matching(brace, other):
                return False
    return len(stack) == 0
