def solution(n):
    count = 0
    for i in range(1, n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += j

            if cur_sum >= n:
                if cur_sum == n:
                    count += 1

                break

    return count
