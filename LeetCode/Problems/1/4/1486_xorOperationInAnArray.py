class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda s, i: s ^ (start + 2 * i), range(n), 0)
