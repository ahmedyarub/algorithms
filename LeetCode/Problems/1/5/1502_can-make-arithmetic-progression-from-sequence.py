class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len(set([arr[i + 1] - arr[i] for i in range(len(arr) - 1)])) == 1
