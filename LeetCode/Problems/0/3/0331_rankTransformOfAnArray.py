class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: r + 1 for r, v in enumerate(sorted(list(set(arr))))}

        return map(ranks.get, arr)
