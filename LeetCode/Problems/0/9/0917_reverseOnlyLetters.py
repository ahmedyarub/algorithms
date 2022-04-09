class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sa = []
        right = len(sa) - 1

        for left, c in enumerate(s):
            if c.isalpha():
                while not s[right].isalpha():
                    right -= 1

                sa.append(s[right])
                right -= 1
            else:
                sa.append(c)

        return "".join(sa)
