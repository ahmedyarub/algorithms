class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx = max([[sum([n if n == 1 else 0 for n in row]), -1 * i] for i, row in enumerate(mat)])
        return [mx[1] * -1, mx[0]]
