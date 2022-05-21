class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return 0 if sum([int(d) for d in str(min(nums))]) % 2 else 1
