class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[r * n:(r + 1) * n] for r in range(m)] if m * n == len(original) else []
