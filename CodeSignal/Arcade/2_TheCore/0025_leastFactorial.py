def solution(n):
    i = fact = 1

    while fact < n:
        i += 1
        fact *= i

    return fact
