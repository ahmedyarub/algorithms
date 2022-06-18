class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return list(
            filter(None, reduce(
                lambda res, d: [word for c in
                                [chr((d - 2) * 3 + (1 if d > 7 else 0) + ord('a') + i)
                                 for i in range(4 if d in [7, 9] else 3)]
                                for word in [prev + c for prev in res]], map(int, list(digits)), [''])))