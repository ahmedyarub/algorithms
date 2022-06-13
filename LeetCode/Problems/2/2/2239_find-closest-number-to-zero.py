class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = nums[0]
        for i in nums:
            if abs(m) >= abs(i):
                if abs(m) == abs(i):
                    m = max(m, i)
                else:
                    m = i
        return m
