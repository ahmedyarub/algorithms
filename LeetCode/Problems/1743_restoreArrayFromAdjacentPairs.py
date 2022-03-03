from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        counts = dict()
        adj = dict()

        def process(num, other_num):
            if num in counts:
                counts[num] += 1
                adj[num].append(other_num)
            else:
                counts[num] = 1
                adj[num] = [other_num]

        for pair in adjacentPairs:
            process(pair[0], pair[1])
            process(pair[1], pair[0])

        start, end = list(filter(lambda key: counts[key] == 1, counts))

        cur = start
        result = [cur]
        seen = set()
        while cur != end:
            seen.add(cur)

            for k in adj[cur]:
                if k not in seen:
                    cur = k
                    break

            result.append(cur)

        return result
