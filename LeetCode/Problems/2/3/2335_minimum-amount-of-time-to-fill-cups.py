class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount) / 2))
