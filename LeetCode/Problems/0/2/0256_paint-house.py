class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def minCost(start: int, previ: int) -> int:
            nonlocal costs

            if start < len(costs):
                return min([cost + minCost(start + 1, i) for i, cost in enumerate(costs[start]) if i != previ])
            else:
                return 0

        return minCost(0, -1)
