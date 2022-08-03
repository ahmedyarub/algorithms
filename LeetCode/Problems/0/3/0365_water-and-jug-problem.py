class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return not ((jug1Capacity + jug2Capacity < targetCapacity) or targetCapacity % gcd(jug1Capacity, jug2Capacity))
