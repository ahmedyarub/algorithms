class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, cnt1, cnt2 = 0, 0, 0

        for num in nums:
            if num:
                cnt1 += 1
            else:
                result = max(result, cnt1 + cnt2 + 1)
                cnt2 = cnt1
                cnt1 = 0

        return min(len(nums), max(result, cnt1 + cnt2 + 1))
