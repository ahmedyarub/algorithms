from itertools import permutations, zip_longest
from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        return words == [''.join(a) for a in zip_longest(*words, fillvalue='')]


if __name__ == '__main__':
    print(Solution().validWordSquare(["abcd", "bnrt", "crm", "dt"]))
