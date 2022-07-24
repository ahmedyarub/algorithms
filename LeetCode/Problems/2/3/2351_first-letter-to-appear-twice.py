class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()

        for c in list(s):
            if c in st:
                return c
            else:
                st.add(c)
