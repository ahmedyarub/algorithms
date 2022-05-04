class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        return sum([1 if n != mn and n != mx else 0 for n in nums])
