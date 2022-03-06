def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(n, m):
    return n + m + gcd(n, m) - 2
