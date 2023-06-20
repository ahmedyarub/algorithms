class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt, has_odd = Counter(s), False

        for c in cnt.values():
            if c // 2 != c / 2:
                has_odd = True
                break

        return sum([c // 2 for c in cnt.values()]) * 2 + (1 if has_odd else 0)
