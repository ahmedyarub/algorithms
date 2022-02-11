def solution(n):
    time = (n // 60) * 100 + n % 60

    total = 0
    while time != 0:
        total += time % 10
        time //= 10

    return total
