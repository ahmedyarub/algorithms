class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        arr2 = [0] * len(arr)
        while changed:
            changed = False
            arr2[0], arr2[-1] = arr[0], arr[-1]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] < arr[i + 1]:
                    arr2[i] = arr[i] + 1
                    changed = True
                elif arr[i - 1] < arr[i] > arr[i + 1]:
                    arr2[i] = arr[i] - 1
                    changed = True
                else:
                    arr2[i] = arr[i]

            arr = arr2.copy()

        return arr
