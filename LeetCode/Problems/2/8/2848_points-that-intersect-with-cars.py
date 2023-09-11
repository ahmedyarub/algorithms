class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        result = biggest = 0

        for start, end in nums:
            result += max(0, end - max(start - 1, biggest))
            biggest = max(biggest, end)

        return result
