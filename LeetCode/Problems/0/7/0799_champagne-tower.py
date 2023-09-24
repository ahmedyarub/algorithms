class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [0.0] * 102
        tower[0] = poured

        for i in range(query_row):
            next_tower = [0.0] * 102

            for j in range(i + 1):
                overflow = max(0.0, (tower[j] - 1.0) / 2.0)
                next_tower[j] += overflow
                next_tower[j + 1] += overflow

            tower = next_tower  # Update the tower for the next row

        return min(1.0, tower[query_glass])
