def solution(scores, n):
    gen = (x**2 for x in sorted(scores, reverse=True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
