class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(ior, nums)
