class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for n in nums if floor(log(n + 1, 10)) % 2])
