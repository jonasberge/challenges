# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    if len(sentence) == 0:
        return sentence
    cursor = 0
    words = []
    for i, char in enumerate(sentence + ' '):
        if char.isnumeric():
            index = int(char)
            continue
        if char == ' ':
            sub = sentence[cursor:i]
            words.append((index - 1, sub))
            cursor = i+1
    parts = [None for _ in range(len(words))]
    for i, word in words:
        parts[i] = word
    return ' '.join(parts)
