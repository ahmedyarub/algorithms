def compose(f, g):
    return lambda a: f(g(a))


def solution(f, g, x):
    return compose(eval(f), eval(g))(x)
