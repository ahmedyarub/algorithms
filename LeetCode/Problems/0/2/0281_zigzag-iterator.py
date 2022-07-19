class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        i, j, self.arr = 0, 0, []
        while i < len(v1) or j < len(v2):
            if i < len(v1):
                self.arr.append(v1[i])
                i += 1
            if j < len(v2):
                self.arr.append(v2[j])
                j += 1
        self.cur = 0

    def next(self) -> int:
        if self.cur < len(self.arr):
            self.cur += 1
            return self.arr[self.cur - 1]

    def hasNext(self) -> bool:
        return self.cur < len(self.arr)
