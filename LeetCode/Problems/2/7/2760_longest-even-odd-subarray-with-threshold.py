class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i, maxi = 0, 0

        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                start = i
                while i < len(nums) - 1 and nums[i] % 2 != nums[i + 1] % 2 and nums[i + 1] <= threshold:
                    i += 1
                sz = i - start + 1
                maxi = max(maxi, sz)

            i += 1

        return maxi
