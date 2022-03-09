def solution(n):
    d = [sum(i % j == 0 for j in range(1, i + 1)) for i in range(1, n + 1)]
    w = [sum(j > m for j in d[:i]) for i, m in enumerate(d)]
    return [max(w), w.count(max(w))]
