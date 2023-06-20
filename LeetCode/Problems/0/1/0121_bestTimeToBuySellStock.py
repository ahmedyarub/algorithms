class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, prof = prices[0], 0

        for price in prices[1:]:
            prof = max(prof, price - mn)
            mn = min(mn, price)

        return prof
