class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [0 ^ first] * (len(encoded) + 1)

        for i, n in enumerate(encoded):
            result[i + 1] = n ^ result[i]

        return result
