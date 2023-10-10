class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans, new_nums, j = n, sorted(set(nums)), 0

        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1

            count = j - i
            ans = min(ans, n - count)

        return ans
