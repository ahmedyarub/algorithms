from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        min_hps = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]

        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                next_hps = []
                if j != len(dungeon[0]) - 1:
                    next_hps.append(min_hps[i][j + 1])
                if i != len(dungeon) - 1:
                    next_hps.append(min_hps[i + 1][j])

                cur_hp = dungeon[i][j] * -1 + min(next_hps, default=0)

                min_hps[i][j] = 0 if cur_hp < 0 else cur_hp

        return min_hps[0][0] + 1
