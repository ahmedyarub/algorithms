class Greeter(object):
    def __init__(self, names):
        self.cnt = 0
        self.names = names

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < len(self.names):
            self.cnt += 1
            return 'Hello, {}!'.format(self.names[self.cnt - 1])
        else:
            raise StopIteration


def solution(team):
    return list(Greeter(team))
