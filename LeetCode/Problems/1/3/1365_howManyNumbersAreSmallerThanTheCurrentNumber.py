class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = dict()
        prev = None
        for i, n in enumerate(sorted(nums)):
            if n != prev:
                count[n] = i
            prev = n

        result = [0] * len(nums)
        for i, n in enumerate(nums):
            result[i] = count[n]

        return result
