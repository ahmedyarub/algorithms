class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def maxdiff(cuts: List[int]):
            diff = float('-inf')
            for i in range(1, len(cuts)):
                diff = max(diff, cuts[i] - cuts[i - 1])

            return diff

        return maxdiff([0] + sorted(horizontalCuts) + [h]) * maxdiff([0] + sorted(verticalCuts) + [w]) % 1000000007
