class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result, n = [], 0

        for num in nums:
            n = n * 2 + num
            result.append(not n % 5)

        return result
