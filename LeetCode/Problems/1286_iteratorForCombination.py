class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.n = combinationLength
        self.i = 0
        self.ans = []
        self.permute('', 0)

    def permute(self, s, start):
        if len(s) == self.n:
            self.ans.append(s)
            return
        else:
            for i in range(start, len(self.c) - self.n + 1 + len(s)):
                self.permute(s + self.c[i], i + 1)

    def next(self) -> str:
        ans = self.ans[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.ans)


if __name__ == '__main__':
    c = CombinationIterator("abcd", 3)
    print(c.ans)
