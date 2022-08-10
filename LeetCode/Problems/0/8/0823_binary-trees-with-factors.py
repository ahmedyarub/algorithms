class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        st = set(arr)

        @cache
        def factors(n: int) -> int:
            result, i, sq = 1, 0, n ** 0.5

            while arr[i] <= sq:
                if not n % arr[i] and n // arr[i] in st:
                    result += (factors(arr[i]) * factors(n // arr[i]) * (1 if arr[i] == n // arr[i] else 2))

                i += 1

            return result

        return sum([factors(num) for num in arr]) % (10 ** 9 + 7)
