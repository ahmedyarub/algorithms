def solution(n):
    return [[0 for i in range(j + 1 if j < n else n - (j - n + 1))] for j in range(2 * n - 1)]
