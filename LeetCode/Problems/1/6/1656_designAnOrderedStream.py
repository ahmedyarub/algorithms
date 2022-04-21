class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value

        start = self.ptr
        while self.ptr < len(self.arr) and self.arr[self.ptr]:
            self.ptr += 1

        return self.arr[start:self.ptr]
