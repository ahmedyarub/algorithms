class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenated = str(n) + str(2 * n) + str(3 * n)

        if '0' in concatenated:
            return False
        if len(concatenated) > 9:
            return False
        for i in range(1, 10):
            if str(i) not in concatenated:
                return False
        return True
