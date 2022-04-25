class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        diff = max(candies) - extraCandies
        return [c >= diff for c in candies]
