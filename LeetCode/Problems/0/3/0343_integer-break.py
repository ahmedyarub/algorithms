class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def ig(num: int) -> int:
            nonlocal n
            return max([ig(num - cur) * cur for cur in range(1, min(n, num + 1))], default=1)

        return ig(n)
