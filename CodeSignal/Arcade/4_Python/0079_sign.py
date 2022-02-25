class Functions(object):
    @staticmethod
    def solution(x):
        return -1 if x < 0 else 1 if x > 0 else 0


def solution(x):
    return Functions.solution(x)
