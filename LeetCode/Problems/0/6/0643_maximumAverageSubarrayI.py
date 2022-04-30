class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = s = sum(nums[:k])

        for i in range(len(nums) - k):
            s = s - nums[i] + nums[i + k]
            result = max(result, s)

        return result / k
