class Solution:
    def isThree(self, n: int) -> bool:
        divs = 2
        for i in range(2, n // 2 + 1):
            if not n % i:
                if divs == 3:
                    return False

                divs += 1

        return divs == 3
