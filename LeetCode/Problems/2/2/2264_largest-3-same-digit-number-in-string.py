class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1

        for i in range(1, len(num) - 1):
            if num[i] == num[i - 1] and num[i] == num[i + 1]:
                result = max(result, int(num[i]))

        return str(result) * 3 if result >= 0 else ""
