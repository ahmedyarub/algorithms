class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            result.extend(map(int, str(num)[:]))

        return result
