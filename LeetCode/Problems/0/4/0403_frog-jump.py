class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mx, st = max(stones), set(stones)

        @cache
        def traverse(k: int, stone: int) -> bool:
            if stone == mx:
                return True

            if stone not in st:
                return False

            return any(
                (
                    traverse(k - 1, k - 1 + stone) if k > 1 else False,
                    traverse(k, k + stone),
                    traverse(k + 1, k + 1 + stone)
                )
            )

        return traverse(1, stones[0] + 1)