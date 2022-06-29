class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result, subs, s = -1, 0, 0
        for i, gc in enumerate(zip(gas, cost)):
            diff = gc[0] - gc[1]
            s += diff
            subs += diff
            if diff >= 0 and (subs < 0 or result == -1):
                subs = diff
                result = i
            elif subs < 0:
                result = -1

        return result if s >= 0 else -1
