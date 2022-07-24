class Solution(object):
    def maxProfit(self, prices):
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            sold, held, reset = (held + price), max(held, reset - price), max(reset, sold)

        return max(sold, reset)
