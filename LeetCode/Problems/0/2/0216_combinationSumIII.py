class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [perm for perm in combinations(range(1, 10), k) if sum(perm) == n]
