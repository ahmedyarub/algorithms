class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0

        for n in nums:
            if not n:
                return 0

            negatives += 1 if n < 0 else 0

        return -1 if negatives % 2 else 1
