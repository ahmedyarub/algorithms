class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * n

        for a, b in trust:
            trust_count[a - 1] = float('-inf')
            trust_count[b - 1] += 1

        for i, c in enumerate(trust_count):
            if c == n - 1:
                return i + 1

        return -1
