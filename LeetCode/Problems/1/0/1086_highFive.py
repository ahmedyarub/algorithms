class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        [d[i].append(s) for i, s in items]

        for i in sorted(d):
            yield i, sum(heapq.nlargest(5, d[i])) // 5
