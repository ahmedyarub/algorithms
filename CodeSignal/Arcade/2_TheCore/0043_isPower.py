def solution(n):
    return not math.sqrt(n) % 1 or 1 >= math.pow(n, 1 / 3) % 1 > 0.99
