class Solution:
    def findPermutation(self, s: str) -> List[int]:
        cur, result, i = len(s) + 1, [0] * (len(s) + 1), len(s) - 1

        while i >= 0:
            if s[i] == 'I':
                result[i + 1] = cur
                cur -= 1
                j = i + 1
                while j < len(s) and s[j] == 'D':
                    result[j + 1] = cur
                    j += 1
                    cur -= 1

            i -= 1

        i = 0
        while cur:
            result[i] = cur
            i += 1
            cur -= 1

        return result
