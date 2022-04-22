from math import sqrt


def square(num):
    p = num * 4
    s = num ** 2
    d = num * sqrt(2)
    return p, s, d


print(square(10))