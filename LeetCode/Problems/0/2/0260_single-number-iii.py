class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        zor = reduce(xor, nums)
        res = reduce(xor, filter(lambda i: i & (zor ^ (zor & (zor - 1))), nums))
        return [res, res ^ zor]
