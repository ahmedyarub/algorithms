def solution(a0):
    seq = [a0]
    while seq[-1] not in seq[:-1]:
        seq.append(sum(int(i) ** 2 for i in str(seq[-1])))
    return len(seq)
