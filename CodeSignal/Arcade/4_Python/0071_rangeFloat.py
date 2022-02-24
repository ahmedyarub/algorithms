class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.i < self.stop:
            self.i += self.step
            return self.i - self.step
        elif self.step < 0 and self.i > self.stop:
            self.i += self.step
            return self.i - self.step
        else:
            raise StopIteration


def solution(args):
    return list(FRange(*args))
