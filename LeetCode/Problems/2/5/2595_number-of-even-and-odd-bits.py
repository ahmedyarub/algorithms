class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result, eo = [0, 0], False

        while n:
            result[int(eo)] += n & 1
            n //= 2
            eo = not eo

        return result
