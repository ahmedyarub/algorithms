class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def traverse(cur: str) -> int:
            if len(cur) == 1:
                return int(1 <= int(cur[0]) <= 9)
            elif len(cur) == 2:
                return (traverse(cur[0]) and traverse(cur[1])) + (10 <= int(cur[0:2]) <= 26)
            else:
                t1 = traverse(cur[1:]) if int(1 <= int(cur[0]) <= 9) else 0
                t2 = traverse(cur[2:]) if (10 <= int(cur[0:2]) <= 26) else 0
                return t1 + t2

        return traverse(s)
