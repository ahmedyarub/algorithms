def solution(a):
    return functools.reduce(lambda result, num: result + [num + result[-1]], a, [0])[1::]
