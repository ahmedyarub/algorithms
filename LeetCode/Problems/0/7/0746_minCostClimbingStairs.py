class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = two = 0
        for i in range(2, len(cost) + 1):
            one, two = min(one + cost[i - 1], two + cost[i - 2]), one

        return one
