def solution(number):
    def fractions():
        a = b = 1
        while True:
            yield [a, b]
            a, b = b, a - 2 * (a % b) + b

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
