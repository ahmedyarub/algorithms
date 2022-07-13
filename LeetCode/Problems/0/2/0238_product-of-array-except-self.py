class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, zeros = reduce(lambda p, n: p * n, list(filter(lambda x: x, nums)) or [0]), nums.count(0)

        if zeros > 1:
            return [0] * len(nums)

        return [(0 if zeros else p // num) if num else p for num in nums]
