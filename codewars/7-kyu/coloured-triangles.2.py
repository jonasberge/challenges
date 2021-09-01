# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111

from collections import deque

dp = {
    'RR': 'R',
    'GG': 'G',
    'BB': 'B',
    'RG': 'B',
    'GR': 'B',
    'GB': 'R',
    'BG': 'R',
    'BR': 'G',
    'RB': 'G',
}

def triangle(row):
    if len(row) == 1:
        return row
    if row in dp:
        return dp[row]
    
    stack = deque()
    stack.append(row)
    while len(stack) != 0:
        item = stack.pop()
        l, r = item[:-1], item[1:]
        if l in dp and r in dp:
            dp[item] = dp[dp[l] + dp[r]]
        if l not in dp or r not in dp:
            stack.append(item)
        if l not in dp:
            stack.append(l)
        if r not in dp:
            stack.append(r)

    return dp[row]
