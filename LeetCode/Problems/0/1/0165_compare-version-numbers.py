class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for num1, num2 in zip_longest(list(map(int, version1.split('.'))), list(map(int, version2.split('.'))),
                                      fillvalue=0):
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        return 0
