def solution(a, b, n):
    return sum([(a + i) * (b + i) for i in range(n)])
