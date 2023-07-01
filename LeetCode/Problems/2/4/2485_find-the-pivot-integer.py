class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right, lsum, rsum = 1, n, 1, n

        while left != right:
            if lsum < rsum:
                left += 1
                lsum += left
            else:
                right -= 1
                rsum += right

        return left if lsum == rsum else -1
