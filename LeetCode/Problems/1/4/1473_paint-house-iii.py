class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def paint(hi: int, nc: int, prevc: int) -> int:
            if hi == m:
                return 0 if nc == target else float('inf')

            if houses[hi]:
                return paint(hi + 1, nc + (houses[hi] != prevc), houses[hi])
            else:
                mcost = float('inf')
                for pi, pcost in enumerate(cost[hi]):
                    mcost = min(mcost, paint(hi + 1, nc + (pi + 1 != prevc), pi + 1) + pcost)

                return mcost

        result = paint(0, 0, 0)
        return result if result != float('inf') else -1
