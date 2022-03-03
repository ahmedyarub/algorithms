def solution(a, b):
    result = 0

    for n in range(a, b + 1):
        while n:
            result += n % 2
            n //= 2

    return result
