class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, first):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    if not first:
                        return False

                    return isPalindrome(s[left:right], False) or isPalindrome(s[left + 1:right + 1], False)

                left += 1
                right -= 1

            return True

        return isPalindrome(s, True)
