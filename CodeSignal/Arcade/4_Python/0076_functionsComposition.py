def compose(functions):
    return functions[0] if len(functions) == 1 else compose([lambda x: functions[0](functions[1](x))] + functions[2:])


def solution(functions, x):
    return compose(map(eval, functions))(x)
