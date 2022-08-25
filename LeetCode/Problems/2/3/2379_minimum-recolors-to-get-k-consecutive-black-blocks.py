class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = blocks[:k].count('W')
        result = cur

        for i in range(k, len(blocks)):
            cur += ((blocks[i] == 'W') - (blocks[i - k] == 'W'))
            result = min(result, cur)

        return result
