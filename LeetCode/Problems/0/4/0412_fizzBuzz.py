class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            s = ""

            if not i % 3:
                s = "Fizz"

            if not i % 5:
                s += "Buzz"

            result.append(str(i) if not s else s)

        return result
