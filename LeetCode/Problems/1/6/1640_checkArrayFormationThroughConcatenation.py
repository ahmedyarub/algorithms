class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        starts = defaultdict(list)

        for piece in pieces:
            starts[piece[0]] = piece

        result = []
        for a in arr:
            result.extend(starts[a])

        return result == arr