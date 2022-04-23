from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBit(n):
            count = 0
            while n:
                n &= n - 1
                count += 1

            return count

        return [n[1] for n in sorted([[countBit(i), i] for i in arr])]


if __name__ == '__main__':
    print(Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
