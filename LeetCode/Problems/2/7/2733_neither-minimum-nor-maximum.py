class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)

        for num in nums:
            if num != mn and num != mx:
                return num

        return -1
