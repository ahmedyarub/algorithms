class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return int(x)

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2

            num = pivot ** 2

            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot

        return right
