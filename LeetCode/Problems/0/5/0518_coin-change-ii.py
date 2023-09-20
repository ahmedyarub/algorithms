class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(rem: int, i: int) -> int:
            if rem < 0 or i == len(coins):
                return 0

            if not rem:
                return 1

            return dp(rem - coins[i], i) + dp(rem, i + 1)

        return dp(amount, 0)
