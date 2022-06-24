class Solution:
    def longestPalindrome(self, s: str) -> int:
        result, odd = 0, False
        for cn in Counter(s).values():
            if cn % 2:
                result += cn - 1
                odd = True
            else:
                result += cn

        return result + odd
