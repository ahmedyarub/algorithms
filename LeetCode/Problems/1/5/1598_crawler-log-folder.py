from functools import reduce


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        return reduce(lambda depth, log: depth + 1 if log != '../' else max(0, depth - 1),
                      [log for log in logs if log != './'], 0)
