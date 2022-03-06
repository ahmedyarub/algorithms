def solution(arr):
    l = len(arr)

    if l % 2:
        middle = arr[l // 2]
    else:
        middle = arr[l // 2] + arr[l // 2 - 1]

    return arr[0] == arr[-1] and arr[0] == middle
