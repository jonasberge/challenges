# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

from collections import defaultdict

def duplicate_encode(word):
    count = defaultdict(lambda: 0)
    for char in word:
        count[char.lower()] += 1
    char_for_count = lambda count: '(' if count == 1 else ')'
    return ''.join(char_for_count(count[c.lower()]) for c in word)
