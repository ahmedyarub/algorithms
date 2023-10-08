class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 < min(nums2):
            return max(nums1) * min(nums2)

        if min(nums1) > 0 > max(nums2):
            return min(nums1) * max(nums2)

        m = len(nums2) + 1
        prev_dp, dp = [0] * m, [0] * m

        for i in range(len(nums1) - 1, -1, -1):
            dp = [0] * m
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, prev_dp[j], dp[j + 1])

            prev_dp = dp

        return dp[0]
