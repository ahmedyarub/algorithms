class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain, cur_gain, result = 0, 0, 0

        for i in range(len(gas)):
            total_gain += (gas[i] - cost[i])
            cur_gain += (gas[i] - cost[i])

            if cur_gain < 0:
                cur_gain = 0
                result = i + 1

        return result if total_gain >= 0 else -1
