class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, f in enumerate(nums):
            for j, g in enumerate(nums):
                if f + g == target:
                    return [i, j]