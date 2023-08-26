class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        return reduce(
            lambda prev, pair: (prev[0] + 1, pair[1]) if prev[1] < pair[0] else (prev[0], prev[1]),
            sorted(pairs, key=lambda x: x[1]),
            (0, float('-inf'))
        )[0]
