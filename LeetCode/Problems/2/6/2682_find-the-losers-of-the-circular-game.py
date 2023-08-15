class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur, st, inc = 0, set([i for i in range(1, n + 1)]), k

        while cur + 1 in st:
            st.remove(cur + 1)
            cur = (cur + inc) % n
            inc += k

        return list(st)
