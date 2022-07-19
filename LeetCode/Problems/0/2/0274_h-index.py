class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1

        i = n
        s = papers[n]
        while i > s:
            i -= 1
            s += papers[i]

        return i
