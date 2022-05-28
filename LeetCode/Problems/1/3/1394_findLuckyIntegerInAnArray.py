class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([v for v, c in Counter(arr).items() if v == c], default=-1)
