class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return [v for v, c in Counter(arr).items() if c > len(arr) // 4][0]
