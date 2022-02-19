from itertools import permutations


def solution(players):
    return sorted(list(permutations(players, 2)))
