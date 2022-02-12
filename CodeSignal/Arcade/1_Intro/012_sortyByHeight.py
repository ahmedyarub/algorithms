def solution(a):
    for i in range(len(a) - 1):
        if a[i] != -1:
            min_pos = i
            for j in range(i + 1, len(a)):
                if a[j] != -1 and a[j] < a[min_pos]:
                    min_pos = j
            a[i], a[min_pos] = a[min_pos], a[i]

    return a
