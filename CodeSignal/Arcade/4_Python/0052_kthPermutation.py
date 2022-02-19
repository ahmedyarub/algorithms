from itertools import permutations


def solution(numbers, k):
    return list(permutations(numbers, len(numbers)))[k - 1]
