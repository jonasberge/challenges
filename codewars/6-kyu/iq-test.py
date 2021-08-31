# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    is_even = None
    even, odd = None, None
    ns = [int(n) for n in numbers.split(' ')]
    for i, n in enumerate(ns, 1):
        if n % 2 == 0:
            if is_even == True:
                return i
            if even is not None:
                if odd is not None:
                    return odd[0]
                is_even = False
            even = (i, n)
        else:
            if is_even == False:
                return i
            if odd is not None:
                if even is not None:
                    return even[0]
                is_even = True
            odd = (i, n)
    raise ValueError('could not determine the odd one out')
