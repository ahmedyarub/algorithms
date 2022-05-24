class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        result, rem = 0, 5000

        for w in sorted(weight):
            rem -= w

            if rem < 0:
                return result

            result += 1

        return result
