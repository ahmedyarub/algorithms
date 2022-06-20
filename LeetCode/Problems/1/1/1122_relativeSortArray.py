class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1 = Counter(arr1)

        r1 = []
        for a2 in arr2:
            r1.extend([a2] * count1.pop(a2))

        return r1 + sorted(count1.elements())
