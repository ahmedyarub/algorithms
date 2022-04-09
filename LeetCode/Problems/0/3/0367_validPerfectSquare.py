class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 1, num // 2

        while left <= right:
            mid = (right - left) // 2 + left
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
