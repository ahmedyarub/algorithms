class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return 10 * (mainTank + min((mainTank - 1) // 4, additionalTank))
