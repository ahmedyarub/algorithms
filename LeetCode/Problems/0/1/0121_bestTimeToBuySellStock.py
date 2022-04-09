from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for _, price in enumerate(prices):
            if price < min_price:
                min_price = price

            cur_profit = price - min_price
            if cur_profit > profit:
                profit = cur_profit

        return profit
