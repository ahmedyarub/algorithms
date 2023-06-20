class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, i = "", 0

        while len(s) - i > len(result) // 2:
            for right in range(i, i + 2):
                left = i
                if right == len(s) or s[left] != s[right]:
                    continue

                cur_str = s[i:right + 1]
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_str = s[left:right + 1]
                    left -= 1
                    right += 1

                if len(result) < len(cur_str):
                    result = cur_str

            i += 1

        return result
