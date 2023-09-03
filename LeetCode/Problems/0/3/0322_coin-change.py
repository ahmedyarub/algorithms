class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q, seen = deque(), set()
        q.append((0, amount))

        while q:
            cnt, rem = q.popleft()

            if not rem:
                return cnt
            elif rem > 0:
                nxt_cnt = cnt + 1
                for coin in coins:
                    nxt_rem = rem - coin
                    if nxt_rem not in seen:
                        q.append((nxt_cnt, nxt_rem))
                        seen.add(nxt_rem)

        return -1
