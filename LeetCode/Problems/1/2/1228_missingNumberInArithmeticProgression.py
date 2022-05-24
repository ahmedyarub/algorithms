from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[0] > arr[-1]:
            arr = arr[::-1]

        step = min([arr[i + 1] - arr[i] for i in range(len(arr) - 1)])

        if not step:
            return arr[0]

        return [n for n in range(arr[0], arr[-1], step) if n not in set(arr)][0]


if __name__ == '__main__':
    print(Solution().missingNumber([15, 13, 12]))
