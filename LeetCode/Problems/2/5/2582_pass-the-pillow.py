class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rem = time % ((n - 1) * 2)

        if rem < n:
            return rem + 1
        else:
            return n - (rem + 1 - n)
