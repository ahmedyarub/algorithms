class PhoneDirectory(set):

    def __init__(self, maxNumbers):
        self.update(range(maxNumbers))

    def get(self):
        return self.pop() if self else -1

    def check(self, number):
        return number in self

    def release(self, number):
        self.add(number)