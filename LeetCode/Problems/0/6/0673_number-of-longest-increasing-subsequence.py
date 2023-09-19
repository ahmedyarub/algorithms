class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length, count = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        mx = max(length)

        return sum(count[i] * (length[i] == mx) for i in range(len(nums)))
