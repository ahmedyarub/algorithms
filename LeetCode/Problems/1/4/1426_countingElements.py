class Solution:
    def countElements(self, arr: List[int]) -> int:
        return sum([1 for n in arr if n + 1 in Counter(arr)])
