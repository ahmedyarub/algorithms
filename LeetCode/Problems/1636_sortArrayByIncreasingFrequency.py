class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        return sorted(nums, key=lambda item: (counts[item], -item))
