class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mc = [0] * m
        nc = [0] * n

        for index in indices:
            mc[index[0]] += 1
            nc[index[1]] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                count += (mc[i] + nc[j]) % 2

        return count
