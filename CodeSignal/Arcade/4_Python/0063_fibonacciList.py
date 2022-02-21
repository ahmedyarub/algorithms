def solution(n):
    return [[0] * x for x in functools.reduce(lambda nums, _: nums + [nums[-1] + nums[-2]], range(n - 2), [0, 1])]
