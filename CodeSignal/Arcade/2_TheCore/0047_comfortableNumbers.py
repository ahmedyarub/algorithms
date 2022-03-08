import itertools


def solution(l, r):
    def is_comfortable(a, b):
        s = sum(int(d) for d in str(a))
        return a - s <= b <= a + s

    cnt = 0
    for a, b in itertools.combinations(range(l, r + 1), 2):
        if is_comfortable(a, b) and is_comfortable(b, a):
            cnt += 1

    return cnt
