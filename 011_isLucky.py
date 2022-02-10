from math import log


def solution(n):
    num_digits = int(log(n, 10)) + 1
    digits_sum = 0

    for i in range(num_digits):
        if i < num_digits / 2:
            digits_sum += n % 10
        else:
            digits_sum -= n % 10

        n = n // 10

    return digits_sum == 0
