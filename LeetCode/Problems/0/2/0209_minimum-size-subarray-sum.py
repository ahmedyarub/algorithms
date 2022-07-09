class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result, li, s = float('inf') if nums[0] < target else 1, 0, nums[0]

        for ri in range(1, len(nums)):
            if result == 1:
                return 1

            s += nums[ri]

            while s >= target and li <= ri:
                s -= nums[li]
                result = min(result, ri - li + 1)
                li += 1

        return 0 if result > len(nums) else result
