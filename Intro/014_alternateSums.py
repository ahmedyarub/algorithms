def solution(a):
    sums = [0, 0]
    sum_index = 0
    for i in range(len(a)):
        sums[sum_index] += a[i]
        sum_index = (sum_index + 1) % 2

    return sums
