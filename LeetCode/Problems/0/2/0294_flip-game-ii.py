from functools import cache


class Solution:
    @cache
    def canWin(self, s):
        return any(s[i:i + 2] == '++' and not self.canWin(s[:i] + '-' + s[i + 2:]) for i in range(len(s)))


if __name__ == '__main__':
    print(Solution().canWin("++++"))
    print(Solution().canWin("+"))
    print(Solution().canWin("+++++"))
