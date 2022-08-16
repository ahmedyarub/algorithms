class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1

        if start not in bank:
            bank.append(start)

        result, seen = float('inf'), set()

        mp = defaultdict(list)
        to = next(i for i, g in enumerate(bank) if g == end)
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if sum([ci != cj for ci, cj in zip(bank[i], bank[j])]) == 1:
                    mp[i].append(j)
                    mp[j].append(i)

        def dfs(fr: int, depth: int):
            nonlocal result, seen
            if depth > result:
                return

            for nxt in mp[fr]:
                if nxt not in seen:
                    if nxt == to:
                        result = min(result, depth)
                        return
                    else:
                        seen.add(fr)
                        dfs(nxt, depth + 1)
                        seen.remove(fr)

        dfs(next(i for i, g in enumerate(bank) if g == start), 1)

        return -1 if result == float('inf') else result
