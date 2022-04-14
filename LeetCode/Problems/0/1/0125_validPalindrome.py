class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [c for c in s.lower() if 'z' >= c >= 'a' or '9' >= c >= '0']
        return arr == arr[::-1]
