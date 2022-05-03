class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == mid and not (mid and arr[mid - 1] == mid - 1):
                return mid
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
