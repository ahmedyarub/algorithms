class Solution(object):
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        if k >= len(prices) // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)

        profits = [0] * len(prices)
        for _ in range(k):
            pre_profit = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i - 1]
                pre_profit = max(pre_profit + profit, profits[i])
                profits[i] = max(profits[i - 1], pre_profit)

        return profits[-1]
