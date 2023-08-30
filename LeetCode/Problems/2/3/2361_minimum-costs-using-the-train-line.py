class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        result = [float('inf')] * len(regular)

        @cache
        def traverse(i, lane):
            if i < 0:
                return 0

            mn = min(regular[i] + traverse(i - 1, False),
                     (0 if lane else expressCost) + express[i] + traverse(i - 1, True))
            result[i] = mn if result[i] == float('inf') else result[i]

            return mn

        traverse(len(regular) - 1, False)

        return result
