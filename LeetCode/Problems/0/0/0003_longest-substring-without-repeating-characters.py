class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frm, st, result = 0, set(), 0

        for i, c in enumerate(s):
            if c in st:
                while c in st:
                    st.remove(s[frm])
                    frm += 1

            st.add(c)
            result = max(result, len(st))

        return result
