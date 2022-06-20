def primesSum(a, b):
    return sum(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(max(2, a), b + 1)))
