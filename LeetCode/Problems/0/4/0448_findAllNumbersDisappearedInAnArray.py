class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        found = [False] * len(nums)

        for n in nums:
            found[n - 1] = True

        result = []
        for i, f in enumerate(found):
            if not f:
                result.append(i + 1)

        return result
