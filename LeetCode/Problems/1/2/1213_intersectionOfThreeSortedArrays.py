class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return [k for k, v in collections.Counter(arr1 + arr2 + arr3).items() if v == 3]
