def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, b = res
    return res
