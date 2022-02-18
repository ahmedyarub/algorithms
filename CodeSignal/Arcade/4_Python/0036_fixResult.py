def solution(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))