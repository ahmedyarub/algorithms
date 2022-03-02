import random


def solution(seed, n):
    class Die(object):
        def __new__(cls, s, n):
            random.seed(s)
            return int(random.random() * n) + 1

    class Game(object):
        die = Die(seed, n)

    return Game.die
