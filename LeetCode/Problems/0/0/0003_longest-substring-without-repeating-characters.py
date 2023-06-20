class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result, known = 0, 0, 0, set()

        while right < len(s):
            c = s[right]

            if c in known:
                while s[left] != c:
                    known.remove(s[left])
                    left += 1

                left += 1
            else:
                known.add(c)

            result = max(result, right - left + 1)
            right += 1

        return result
