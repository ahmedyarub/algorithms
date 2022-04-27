class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ops = [1, 2, 4, 8, 16, 32, 60, 120, 240, 480]

        result = []
        for comb in combinations(ops, turnedOn):
            if 32 in comb and 16 in comb and 8 in comb and 4 in comb:
                continue

            s = sum(comb)
            hour, s = divmod(s, 60)
            if hour > 11:
                continue

            minute, s = divmod(s, 10)

            result.append(str(hour) + ":" + str(minute) + str(s))

        return result
