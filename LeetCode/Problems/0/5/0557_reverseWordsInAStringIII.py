class Solution:
    def reverseWords(self, s: str) -> str:
        i1, i2 = 0, 0
        result = []
        while i2 <= len(s):
            if i2 == len(s) or s[i2] == " ":
                result += [s[i1:i2][::-1]]

                i1 = i2 + 1

            i2 += 1

        return " ".join(result)
