class Solution:
    def reverseVowels(self, s: str) -> str:
        sarr = [c for c in s]
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        while True:
            while left < len(s) and sarr[left].lower() not in vowels:
                left += 1

            while right >= 0 and sarr[right].lower() not in vowels:
                right -= 1

            if left >= right:
                return "".join(sarr)

            sarr[left], sarr[right] = s[right], s[left]
            left += 1
            right -= 1
