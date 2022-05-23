class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T = sum(calories[:k])
        pts = (T > upper) - (T < lower)
        for i in range(k, len(calories)):
            T += (calories[i] - calories[i - k])
            pts += ((T > upper) - (T < lower))
        return pts