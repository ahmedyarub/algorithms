class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0

        for c in s:
            if c == 'L':
                late += 1
                if late == 3:
                    return False

                continue

            if c == 'A':
                absent += 1
                if absent == 2:
                    return False

            late = 0

        return True
