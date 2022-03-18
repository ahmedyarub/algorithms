from itertools import permutations


def solution(inputArray):
    perms = permutations(inputArray)
    for perm in perms:
        if not sum([sum([c1 != c2 for c1, c2 in zip(perm[i], perm[i + 1])]) != 1 for i in range(len(perm) - 1)]):
            return True

    return False
