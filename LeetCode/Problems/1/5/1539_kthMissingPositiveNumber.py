class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (right + left) // 2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k
