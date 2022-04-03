class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            pivot = (left + right) >> 1

            if isBadVersion(pivot):
                if pivot == 1 or not isBadVersion(pivot - 1):
                    return pivot

                right = pivot - 1
            else:
                left = pivot + 1
