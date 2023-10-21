from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = SortedList([0])
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])

        return max(dp)
