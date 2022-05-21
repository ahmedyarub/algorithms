class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = collections.defaultdict(int)

        for domino in dominoes:
            counter[tuple(sorted(domino))] += 1

        return sum([v * (v - 1) // 2 for v in counter.values()])
