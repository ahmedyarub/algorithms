class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        result, results = float('inf'), defaultdict(int)

        def traverse(start: int, remaining: int, cnt: int):
            nonlocal result

            if not remaining:
                result = cnt
                return

            if cnt >= result or start >= len(coins):
                return

            if results[remaining] and results[remaining] <= cnt:
                return
            else:
                results[remaining] = cnt

            for j in range(start, len(coins)):
                remain = remaining - coins[j]

                if remain < 0:
                    continue

                traverse(i if remain >= coins[i] else i + 1, remain, cnt + 1)

        for i in range(len(coins)):
            traverse(i, amount, 0)

        return -1 if result == float('inf') else result
