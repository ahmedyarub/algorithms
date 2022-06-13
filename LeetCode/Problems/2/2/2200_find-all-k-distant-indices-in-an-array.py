class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        high = -1
        n = len(nums)

        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(high + 1, i - k), min(n, i + k + 1)):
                    res.append(j)
                high = i + k

        return res
