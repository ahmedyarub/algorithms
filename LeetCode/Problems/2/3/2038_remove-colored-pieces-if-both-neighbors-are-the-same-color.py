class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        prev, cnt = None, defaultdict(int)

        for ci in range(1, len(colors) - 1):
            if colors[ci - 1] == colors[ci] == colors[ci + 1]:
                cnt[colors[ci]] += 1

        return cnt['A'] > cnt['B']
