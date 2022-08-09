class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        cur_sum = sum([i * j for i, j in enumerate(nums)])
        ans = cur_sum

        for i in range(n):
            ans = max(ans, cur_sum := cur_sum + s - nums[n - 1 - i] * n)

        return ans
