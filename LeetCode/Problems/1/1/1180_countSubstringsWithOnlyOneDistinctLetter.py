class Solution:
    def countLetters(self, s: str) -> int:
        prev, result, cur = '', 0, 0

        for c in s + ' ':
            if c != prev:
                result += cur * (cur + 1) // 2
                prev = c
                cur = 0

            cur += 1

        return result
