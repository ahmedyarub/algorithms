class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        result = 0
        for b in bank:
            cur = sum(int(c) for c in b)

            if cur:
                result += (cur * prev)
                prev = cur

        return result
