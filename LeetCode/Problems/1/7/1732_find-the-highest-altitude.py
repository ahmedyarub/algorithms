class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate([0] + gain, operator.add))
