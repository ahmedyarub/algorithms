def solution(arr):
    l = len(arr)

    if not l % 2:
        arr[l // 2 - 1] += arr[l // 2]
        del arr[l // 2]

    return arr
