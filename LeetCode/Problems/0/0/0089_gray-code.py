class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        arr = self.grayCode(n - 1)
        return arr + [(1 << (n - 1)) + k for k in arr[::-1]]
