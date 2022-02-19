from itertools import takewhile, count


def solution(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)
