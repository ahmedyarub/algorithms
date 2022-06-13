class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(not cnt % 2 for cnt in Counter(nums).values())
