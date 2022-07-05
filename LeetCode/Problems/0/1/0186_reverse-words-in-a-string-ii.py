class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1

            end = i - 1
            i += 1

            while end > start:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
