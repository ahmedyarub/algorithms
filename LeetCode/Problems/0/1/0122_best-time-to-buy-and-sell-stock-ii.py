class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx, result = prices[0], prices[0], 0

        for p in prices[1:]:
            if p < mx:
                result += mx - mn
                mn = mx = p
            elif p < mn:
                mn = p

            if p > mx:
                mx = p

        return result + mx - mn
