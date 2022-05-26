class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        arr[-1] = -1
        for i, n in enumerate(arr[-2::-1]):
            arr[-i - 2] = mx
            mx = max(mx, n)

        return arr
