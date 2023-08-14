class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        ans, s1, s2 = 0, 0, 0
        n = len(player1)
        for i in range(n):
            s1 += player1[i]
            s2 += player2[i]
        if n > 1:
            for i in range(1, n):
                if player1[i - 1] == 10 or ((i >= 2) and player1[i - 2] == 10):
                    s1 += player1[i]
                if player2[i - 1] == 10 or ((i >= 2) and player2[i - 2] == 10):
                    s2 += player2[i]

        return 1 if s1 > s2 else (2 if s2 > s1 else 0)
