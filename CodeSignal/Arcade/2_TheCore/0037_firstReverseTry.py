def solution(arr):
    if len(arr) > 0:
        arr[0], arr[-1] = arr[-1], arr[0]

    return arr
