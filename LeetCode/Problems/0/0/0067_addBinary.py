class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai, bi, result, car = len(a) - 1, len(b) - 1, [], 0

        while ai >= 0 or bi >= 0:
            an, bn = int(a[ai]) if ai >= 0 else 0, int(b[bi]) if bi >= 0 else 0
            s = an + bn + car

            result.append('0' if s == 0 or s == 2 else '1')
            car = 1 if s > 1 else 0

            ai -= 1
            bi -= 1

        if car:
            result.append('1')

        return ''.join(reversed(result))
