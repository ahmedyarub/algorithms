class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = nums[0]
        cur = 1
        mx = 1
        for num in nums:
            if num > prev:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 1

            prev = num

        return mx
