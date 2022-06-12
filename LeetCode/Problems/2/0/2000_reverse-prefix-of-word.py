class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        p = word.find(ch)

        return (word[:p + 1])[::-1] + word[p + 1:]
