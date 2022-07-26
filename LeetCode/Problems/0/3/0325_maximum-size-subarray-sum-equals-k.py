class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum, longest_subarray, indices = 0, 0, {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum - k in indices:
                longest_subarray = max(longest_subarray, i - indices[prefix_sum - k])

            if prefix_sum not in indices:
                indices[prefix_sum] = i

        return longest_subarray
