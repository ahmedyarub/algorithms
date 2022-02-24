class Solution:
    def calcSum(self, n):
        sum = 0

        while n:
            sum += (n % 10) ** 2
            n //= 10

        return sum

    def isHappy(self, n: int) -> bool:
        cur_sum = self.calcSum(n)
        known = set()

        while cur_sum != 1:
            if cur_sum in known:
                return False

            known.add(cur_sum)
            cur_sum = self.calcSum(cur_sum)

        return True
