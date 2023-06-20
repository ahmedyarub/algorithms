class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda pair: pair[0], sorted(Counter(nums).vehicles(), key=lambda pair: pair[1], reverse=True)[:k]))