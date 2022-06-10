class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        d = 0
        while True:
            i = start + d
            if i < len(nums) and nums[i] == target:
                return d

            i = start - d
            if i >= 0 and nums[i] == target:
                return d

            d += 1
