class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt, num1, num2 = 0, min(num1, num2), max(num1, num2)
        while num1 and num2:
            num1, num2 = num2 - num1, num1
            num1, num2 = min(num1, num2), max(num1, num2)
            cnt += 1

        return cnt
