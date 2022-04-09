class Solution:
    def sortSentence(self, s: str) -> str:
        strs = s.split()
        result = [""] * len(strs)

        for word in strs:
            result[int(word[-1]) - 1] = word[:(len(word) - 1)]

        return " ".join(result)
