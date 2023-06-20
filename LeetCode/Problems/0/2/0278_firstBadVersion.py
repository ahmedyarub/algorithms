# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            bad = isBadVersion(mid + 1)
            if bad:
                if not mid or not isBadVersion(mid):
                    return mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1
