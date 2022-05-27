class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            lo = 0
            hi = len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        if not s:
            return 0
        if is_palindrome(s):
            return 1
        return 2
