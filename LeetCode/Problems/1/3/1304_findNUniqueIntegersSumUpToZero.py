class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2:
            result = [0]
        else:
            result = []

        for i in range(1, 1 + n // 2):
            result.append(i)
            result.append(-1 * i)

        return result
