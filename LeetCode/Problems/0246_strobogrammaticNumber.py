class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirrors = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        for i in range(ceil(len(num) / 2)):
            if num[i] not in mirrors or mirrors[num[i]] != num[len(num) - i - 1]:
                return False

        return True
