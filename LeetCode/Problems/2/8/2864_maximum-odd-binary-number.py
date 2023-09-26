class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_ones = s.count('1')
        return "".join(['1'] * (cnt_ones - 1) + ['0'] * (len(s) - cnt_ones) + ['1'])
