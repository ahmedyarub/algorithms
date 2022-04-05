class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber:
            result = chr(ord('A') + (columnNumber - 1) % 26) + result
            columnNumber = (columnNumber - 1) // 26

        return result
