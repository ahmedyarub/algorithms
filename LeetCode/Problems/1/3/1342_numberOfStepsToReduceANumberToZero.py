class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0

        while num:
            counter += 1
            if num % 2:
                num -= 1
            else:
                num //= 2

        return counter
