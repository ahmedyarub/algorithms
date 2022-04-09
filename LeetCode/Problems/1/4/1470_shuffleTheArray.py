class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [None] * n * 2
        for i in range(n):
            result[i * 2] = nums[i]
            result[i * 2 + 1] = nums[i + n]

        return result
