class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = 1
        for d in range(2, ceil(sqrt(num))):
            if not num % d:
                s += d

                if d != num // d:
                    s += num // d

        return s == num
