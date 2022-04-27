class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        for comb in permutations(digits, 3):
            if not comb[0] or comb[-1] % 2:
                continue

            result.add(comb[0] * 100 + comb[1] * 10 + comb[2])

        return sorted(list(result))
