class Prizes(object):
    def __init__(self, purchases, step, condition):
        self.purchases = purchases
        self.step = step
        self.condition = condition

    def __iter__(self):
        for i in range(self.step - 1, len(self.purchases), self.step):
            if self.purchases[i] % self.condition == 0:
                yield i + 1


def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
