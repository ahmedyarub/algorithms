class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = dict()
        ts = dict()

        for i, j in zip(s, t):
            if i not in st and j not in ts:
                st[i], ts[j] = j, i
            elif st.get(i) != j or ts.get(j) != i:
                return False

        return True
