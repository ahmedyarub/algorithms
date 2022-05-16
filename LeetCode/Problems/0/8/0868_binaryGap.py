class Solution:
    def binaryGap(self, n: int) -> int:
        result, cur = 0, 0
        for d in bin(n)[2:]:
            if d == '0':
                cur += 1
            else:
                result = max(result, cur)
                cur = 1

        return result
