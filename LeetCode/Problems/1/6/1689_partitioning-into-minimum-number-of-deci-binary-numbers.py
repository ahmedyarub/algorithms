class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(map(int, list(n))))
