def solution(n):
    x = 1
    while n > 10:
        n = (n + 5) // 10
        x *= 10
    return x * n
