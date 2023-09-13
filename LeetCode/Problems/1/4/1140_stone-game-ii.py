class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(p: int, i: int, m: int) -> int:
            if i == len(piles):
                return 0

            res, s = 1000000 if p == 1 else -1, 0
            for x in range(1, min(2 * m, len(piles) - i) + 1):
                s += piles[i + x - 1]

                if not p:
                    res = max(res, s + dp(1, i + x, max(m, x)))
                else:
                    res = min(res, dp(0, i + x, max(m, x)))

            return res

        return dp(0, 0, 1)
