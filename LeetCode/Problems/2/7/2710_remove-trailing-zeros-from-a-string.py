class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        limit = len(num)

        while limit > 0 and num[limit - 1] == '0':
            limit -= 1

        return num[:limit]
