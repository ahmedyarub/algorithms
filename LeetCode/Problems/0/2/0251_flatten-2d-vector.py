class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec, self.row, self.col = [ls for ls in vec if len(ls)], 0, 0

    def next(self) -> int:
        res = self.vec[self.row][self.col]

        if self.col == len(self.vec[self.row]) - 1:
            self.row += 1
            self.col = 0
        else:
            self.col += 1

        return res

    def hasNext(self) -> bool:
        return self.row < len(self.vec)
