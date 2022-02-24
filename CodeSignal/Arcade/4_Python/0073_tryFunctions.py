def solution(x, functions):
    return [eval(i)(x) for i in functions]
