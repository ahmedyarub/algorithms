class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, cur = 0, 0

        for n in nums:
            if n:
                cur += 1
            else:
                result = max(result, cur)
                cur = 0

        return max(result, cur)
