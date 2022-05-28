class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        l2 = len(arr2)
        distance_value = 0

        for n1 in arr1:
            index = bisect.bisect_left(arr2, n1 - d)
            index = min(l2 - 1, index)
            n2 = arr2[index]

            if abs(n1 - n2) > d:
                distance_value += 1

        return distance_value
