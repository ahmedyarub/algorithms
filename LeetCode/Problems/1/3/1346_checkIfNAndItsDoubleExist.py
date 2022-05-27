class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counts = Counter(arr)

        for n in arr:
            if n == 0:
                if counts[0] > 1:
                    return True
            elif (n * 2) in counts:
                return True

        return False
