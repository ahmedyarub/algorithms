class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, cnts, l, r, mxf = 0, defaultdict(int), 0, -1, 0

        while r < len(s) - 1:
            r += 1

            cnts[s[r]] += 1
            mxf = max(mxf, cnts[s[r]])
            window = r - l + 1
            others = window - mxf
            if others <= k:
                result = window
            else:
                cnts[s[l]] -= 1
                l += 1

        return result
