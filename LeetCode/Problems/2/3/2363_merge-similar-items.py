class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        st = set()

        mp1 = defaultdict(int)
        for n1, w1 in items1:
            st.add(n1)
            mp1[n1] = w1

        mp2 = defaultdict(int)
        for n2, w2 in items2:
            st.add(n2)
            mp2[n2] = w2

        return [[n, mp1[n] + mp2[n]] for n in sorted(st)]
