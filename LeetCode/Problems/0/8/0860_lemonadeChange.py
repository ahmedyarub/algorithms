class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            b[bill] += 1

            remaining = bill - 5

            if remaining >= 10:
                if b[10] > 0:
                    remaining -= 10
                    b[10] -= 1

            if remaining > 0:
                if b[5] >= remaining / 5:
                    b[5] -= remaining / 5
                else:
                    return False

        return True
