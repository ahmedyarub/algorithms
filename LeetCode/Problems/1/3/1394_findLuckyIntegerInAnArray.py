class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([v for v, c in Counter(arr).vehicles() if v == c], default=-1)
