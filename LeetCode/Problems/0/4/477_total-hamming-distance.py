class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        digits = int(log(max(nums), 2) + 1)

        counts = [[0] * digits for _ in range(2)]

        for num in nums:
            for digit in range(digits):
                counts[((1 << digit) & num) > 0][digit] += 1

        return sum(counts[0][digit] * counts[1][digit] for digit in range(digits))
