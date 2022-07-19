class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = [1]

        while n > 1:
            n -= 1
            num = heappop(hp)

            while hp and hp[0] == num:
                heappop(hp)

            heappush(hp, num * 2)
            heappush(hp, num * 3)
            heappush(hp, num * 5)

        return heappop(hp)
