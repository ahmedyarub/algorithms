from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        mn, mx = nums.index(1), nums.index(n := len(nums))
        return mn - mx + n - 1 - (mn > mx)
