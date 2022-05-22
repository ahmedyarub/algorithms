class Solution:
    def tribonacci(self, n: int) -> int:
        trib, i = [0, 1, 1], 3

        while i <= n:
            trib.append(sum(trib[i - 3:i]))
            i += 1

        return trib[n]
