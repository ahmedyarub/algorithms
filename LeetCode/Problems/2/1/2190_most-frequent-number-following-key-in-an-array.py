class Solution:
    def mostFrequent(self, nums, key):
        return max(c := Counter([nums[i] for i in range(1, len(nums)) if nums[i - 1] == key]), key=c.get)
