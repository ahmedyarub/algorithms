class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum(1 if sum(q[0:3]) == q[3] else 0 for q in combinations(nums, 4))
