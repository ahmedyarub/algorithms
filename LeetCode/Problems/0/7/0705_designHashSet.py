class MyHashSet:

    def __init__(self):
        self.hs = [None] * (10 ** 7)

    def add(self, key: int) -> None:
        self.hs[key] = key

    def remove(self, key: int) -> None:
        self.hs[key] = None

    def contains(self, key: int) -> bool:
        return self.hs[key] is not None
