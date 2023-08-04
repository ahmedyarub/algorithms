class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        if money > 8 * children:
            return children - 1

        money -= children

        res, extra = divmod(money, 7)

        if extra == 3 and res + 1 == children:
            return res - 1

        return res
