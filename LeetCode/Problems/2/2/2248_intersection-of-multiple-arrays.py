class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(list(reduce(lambda p, c: set(p) & set(c), nums)))
