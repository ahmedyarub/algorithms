class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dic = [0] * n
        dic[0], dic[1] = 1, 2

        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] == 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)

        return dic[n]


if __name__ == '__main__':
    print(Solution().climbStairs(2))
