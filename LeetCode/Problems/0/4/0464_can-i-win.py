class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def can_player_win_on(target: int, bitflag: int) -> bool:
            if target <= 0:
                return False

            for call_number in range(1, maxChoosableInteger + 1):
                if bitflag & (1 << call_number):
                    continue

                if not can_player_win_on(target - call_number, bitflag | (1 << call_number)):
                    return True

            return False

        max_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if max_sum < desiredTotal:
            return False

        elif desiredTotal <= 0:
            return True

        elif max_sum == desiredTotal and maxChoosableInteger % 2:
            return True

        return can_player_win_on(desiredTotal, 0)
