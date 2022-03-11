def solution(n):
    return all([not int(i) % 2 for i in str(n)])
