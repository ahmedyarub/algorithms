class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mx1, mx0, zeros, ones = 0, 0, 0, 0

        for c in s:
            if c == '1':
                mx0 = max(mx0, zeros)
                zeros = 0
                ones += 1
                mx1 = max(mx1, ones)
            else:
                mx1 = max(mx1, ones)
                ones = 0
                zeros += 1
                mx0 = max(mx0, zeros)

        return mx1 > mx0
