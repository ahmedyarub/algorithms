class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ns = str(num)
        return sum([not num % int(ns[i:i + k]) for i in range(len(ns) - k + 1) if int(ns[i:i + k])])
