# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    if len(s) == 0:
        return False
    parts = []
    for word in s.split(' '):
        parts.append(word.capitalize())
    if len(parts) == 0:
        return False
    res = '#' + ''.join(parts)
    if len(res) > 140:
        return False
    return res
