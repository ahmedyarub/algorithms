class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def conv(s):
            return reduce(lambda res, c: res * 10 + ord(c) - ord('a'), list(s), 0)

        return conv(firstWord) + conv(secondWord) == conv(targetWord)
