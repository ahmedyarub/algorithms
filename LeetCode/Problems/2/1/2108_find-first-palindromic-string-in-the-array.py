class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")
