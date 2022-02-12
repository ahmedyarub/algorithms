def solution(min1, min2_10, min11, s):
    total = 0

    if s >= min1:
        total = 1
        s -= min1
    else:
        return total

    if s >= min2_10:
        if min2_10 * 9 > s:
            return total + (s // min2_10)

        total += 9
        s -= (9 * min2_10)
    else:
        return total

    return total + (s // min11)
