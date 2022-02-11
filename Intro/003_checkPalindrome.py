import itertools


def solution(inputString):
    return all(i == j for i, j in itertools.islice(zip(inputString, reversed(inputString)), 0, len(inputString) // 2))
