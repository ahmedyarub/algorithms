class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1

        neg, n = n < 0, abs(n)

        @lru_cache(maxsize=None)
        def calc(l: int, d: int) -> int:
            return l if d == 1 else calc(l, d // 2) * calc(l, ceil(d / 2))

        res = calc(x, n)

        return 1 / res if neg else res
