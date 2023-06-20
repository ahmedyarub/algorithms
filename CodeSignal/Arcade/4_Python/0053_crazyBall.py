from itertools import combinations


def solution(players, k):
    return list(combinations(sorted(players), k))