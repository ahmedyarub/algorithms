class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        mul1, mul2 = (purchaseAmount // 10) * 10, ((purchaseAmount // 10) + 1) * 10

        if abs(mul1 - purchaseAmount) < abs(mul2 - purchaseAmount):
            return 100 - mul1
        else:
            return 100 - mul2
