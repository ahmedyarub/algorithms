class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = sum(not n for n in arr)

        slow, fast = len(arr) + zeros - 1, len(arr) - 1

        while fast >= 0:
            if not arr[fast]:
                if slow < len(arr):
                    arr[slow] = 0
                slow -= 1

            if slow < len(arr):
                arr[slow] = arr[fast]

            slow -= 1
            fast -= 1
