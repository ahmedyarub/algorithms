def solution(a, b):
    differences = 0
    dif_index = -1

    for i in range(len(a)):
        if a[i] != b[i]:
            if differences > 1:
                return False
            if differences == 1:
                if a[dif_index] != b[i] or b[dif_index] != a[i]:
                    return False
                else:
                    differences = 2
            else:
                differences = 1
                dif_index = i
    return True
