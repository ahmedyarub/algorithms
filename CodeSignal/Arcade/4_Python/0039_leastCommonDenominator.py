from math import gcd


def solution(denominators):
    return functools.reduce(lambda a, b: a * b // gcd(a, b), denominators)
