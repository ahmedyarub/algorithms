class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left * 2 < right:
            return 0

        result = left
        while result > 0 and left <= right:
            result &= left
            left += 1

        return result
