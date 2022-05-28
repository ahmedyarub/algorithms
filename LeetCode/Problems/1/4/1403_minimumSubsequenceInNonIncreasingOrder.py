class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        nums.sort()
        result, right = [], 0

        for num in reversed(nums):
            result.append(num)
            right += num
            if right > s - right:
                return result

        return []
