class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return max([[sum([0 if n % d else 1 for n in nums]), d * -1] for d in divisors])[1] * -1
