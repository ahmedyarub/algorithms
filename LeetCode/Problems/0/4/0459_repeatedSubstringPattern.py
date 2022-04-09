class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        i = 0
        while i < len(s):
            i += 1
            while i < len(s) and s[i] != s[0]:
                i += 1

            if i == len(s):
                return False

            if len(s) % (i):
                continue

            substr = s[:i]

            s_i = i
            sub_i = 0
            found = True
            while s_i < len(s):
                if substr[sub_i] != s[s_i]:
                    found = False
                    break
                s_i += 1
                sub_i = (sub_i + 1) % len(substr)

            if found:
                return True

        return False
