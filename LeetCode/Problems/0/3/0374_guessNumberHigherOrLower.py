# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while True:
            mid = (left + right) // 2
            g = guess(mid)

            if g == -1:
                right = mid - 1
            elif g == 1:
                left = mid + 1
            else:
                return mid
