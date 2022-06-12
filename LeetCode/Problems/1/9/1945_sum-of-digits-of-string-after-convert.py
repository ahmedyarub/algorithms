class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = "".join([str(ord(c) - ord('a') + 1) for c in s])
        for _ in range(k):
            n = str(sum([int(ch) for ch in n]))

        return int(n)
