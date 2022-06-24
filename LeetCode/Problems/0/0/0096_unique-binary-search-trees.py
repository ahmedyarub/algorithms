class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def traverse(start: int, end: int) -> int:
            if start > end:
                return 1

            cnt = 0

            for i in range(start, end + 1):
                cnt += (traverse(start, i - 1) * traverse(i + 1, end))

            return cnt

        return traverse(1, n)
