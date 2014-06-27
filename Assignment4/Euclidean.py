from math import *

def gcd(a, b):  # a != 0, b != 0
    r = a % b
    x = min(a, b)
    while (r != 0):
        if r < x:
            d = r
            r = x % r
            x = d
        elif r == x:
            x = max(a, b)
    return x



